//
//  lkm_test.c
//  
//
//  Created by Gustavo Cordido on 4/11/20.
//
#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/netfilter.h>
#include <linux/netfilter_ipv4.h>
#include <linux/ip.h>
#include <linux/tcp.h>
#include <linux/udp.h>
#include <linux/fs.h>
#include <asm/segment.h>
#include <asm/uaccess.h>
#include <linux/buffer_head.h>

#define PORT_1 5627
#define PORT_2 8080

//Netfilter Hook Structure
static struct nf_hook_ops *nfho = NULL;

struct networkingInfo {
    u32 srcIP, dstIP;
    unsigned int package_count;
} networkingInfo;

int count = 0;

struct networkingInfo connection_arr[1000];

static unsigned int packets(const struct nf_hook_ops *ops, struct sk_buff *skb, const struct net_device *in, const struct net_device *out, int (*okfn)(struct sk_buff *)){
    
    struct iphdr *ip_header;
    struct tcphdr *tcp_header;
    u16 sport;
    u16 dport;
    u32 saddr;
    u32 daddr;
    
    ip_header = ip_hdr(skb);
    
    tcp_header = tcp_hdr(skb);
    
    saddr= ntohl(ip_header->saddr);
    daddr = ntohl(ip_header->daddr);
    sport = ntohs(tcp_header->source);
    dport = ntohs(tcp_header->dest);
    
    int pos = 0, isNew = 1, i;
    
    for(i=0; i<count; i++){
        if(connection_arr[i].srcIP == saddr && connection_arr[i].dstIP == daddr){
            connection_arr[i].package_count++;
            isNew = 0;
            pos = i;
            break;
        }
    }
    
    if(count == 0 || count < 1000 && isNew == 1){
        connection_arr[count].srcIP = saddr;
        connection_arr[count].dstIP = daddr;
        connection_arr[count].package_count = 1;
        pos = count;
        count++;
    }
    
    printk("%pI4h, %pI4h, %d\n", &saddr, &daddr, connection_arr[pos].package_count);
    
    return NF_ACCEPT;
}

static int hook_setup(void) {
    nfho = (struct nf_hook_ops*)kcalloc(1, sizeof(struct nf_hook_ops), GFP_KERNEL);
    
    nfho->hook = (nf_hookfn*) packets;    //hook function is called in here
    nfho->hooknum = NF_INET_PRE_ROUTING;        //recieved packets
    nfho->pf = PF_INET;                            //IPv4
    nfho->priority = NF_IP_PRI_FIRST;            //max hook priority

    nf_register_net_hook(&init_net, nfho);
    return 0;
}

static void hook_exit(void) {
    nf_unregister_net_hook(&init_net, nfho);
    kfree(nfho);
}

    module_init(hook_setup);
    module_exit(hook_exit);

    

MODULE_AUTHOR("Gustavo");
MODULE_LICENSE("GPL");
MODULE_DESCRIPTION("LKM for Docker Networking Topology");
