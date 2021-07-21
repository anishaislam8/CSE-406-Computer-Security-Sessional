/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package dhcpstarvation;

/**
 *
 * @author gahab
 */
public class DHCP_Packet {
    private String type;
    private String srcPort;
    private String destPort;
    private String srcIP;
    private String destIP;
    private String chaddr;
    private String ciaddr;
    private String yiaddr;
    private String siaddr;
    private String giaddr;
    private String xid;
   
   
    

    public void setChaddr(String chaddr) {
        this.chaddr = chaddr;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getType() {
        return type;
    }

    public void setCiaddr(String ciaddr) {
        this.ciaddr = ciaddr;
    }

    public void setYiaddr(String yiaddr) {
        this.yiaddr = yiaddr;
    }

    public void setSiaddr(String siaddr) {
        this.siaddr = siaddr;
    }

    public void setGiaddr(String giaddr) {
        this.giaddr = giaddr;
    }

    public void setXid(String xid) {
        this.xid = xid;
    }

    public void setDestPort(String destPort) {
        this.destPort = destPort;
    }

    public void setSrcPort(String srcPort) {
        this.srcPort = srcPort;
    }

    public void setDestIP(String destIP) {
        this.destIP = destIP;
    }

    public void setSrcIP(String srcIP) {
        this.srcIP = srcIP;
    }

    public String getChaddr() {
        return chaddr;
    }

    public String getCiaddr() {
        return ciaddr;
    }

    public String getYiaddr() {
        return yiaddr;
    }

    public String getSiaddr() {
        return siaddr;
    }

    public String getGiaddr() {
        return giaddr;
    }

    public String getXid() {
        return xid;
    }

    public String getDestPort() {
        return destPort;
    }

    public String getSrcPort() {
        return srcPort;
    }

    public String getDestIP() {
        return destIP;
    }

    public String getSrcIP() {
        return srcIP;
    }

    public DHCP_Packet(String type, String srcPort, String destPort, String srcIP, String destIP,  String ciaddr, String yiaddr, String siaddr, String giaddr,String chaddr, String xid) {
        this.type = type;
        this.srcPort = srcPort;
        this.destPort = destPort;
        this.srcIP = srcIP;
        this.destIP = destIP;
        this.chaddr = chaddr;
        this.ciaddr = ciaddr;
        this.yiaddr = yiaddr;
        this.siaddr = siaddr;
        this.giaddr = giaddr;
        this.xid = xid;
    }

    
}
