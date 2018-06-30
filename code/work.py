# -*- coding:utf-8 -*-
import urllib2
import json
def look_firestat():
	print '================FirewallState(防火墙状态)================='
	url="http://127.0.0.1:8080/firewall/module/status"
	data=urllib2.Request(url)
	res_data=urllib2.urlopen(data)
	res=res_data.read()
	res=json.loads(res)
	print res
	if(res[0]['switch_id']=='0000000000000001'):
		print 'swithc is %s'%res[0]['switch_id']
	return res
def enable_firewall(dp):
	print "================EnableFirewall(使能防火墙)==============="
	url='http://127.0.0.1:8080/firewall/module/enable/'+dp
	print data
	req = urllib2.Request(url)
	req.add_header('Content-Type', 'your/contenttype')
	req.get_method = lambda: 'PUT'
	res= urllib2.urlopen(req)
	res_data=res.read()
	print res_data
#防火墙rule集合
def rule_firewall(dp):
	print "================FirwallRules(防火墙Rules)=================="
	url='http://127.0.0.1:8080/firewall/rules/'+dp
	print url
	req=urllib2.Request(url)
	res_data=urllib2.urlopen(req)
	res=res_data.read().decode('utf8')
	res=json.loads(res)
	print res
#添加广播规则
def add_Brodcastrule(dp,nw_src,nw_dst):
	print "=================AddFirewallRule(添加规则Rule)=============="
	url='http://127.0.0.1:8080/firewall/rules/'+dp
	data={"nw_src":nw_src, "nw_dst": nw_dst}
	
	req=urllib2.Request(url,json.dumps(data))
	response=urllib2.urlopen(req)
	res=response.read().encode('utf8')
	print res
#添加规则
def add_rule(dp,nw_src,nw_dst,nw_proto,port,action,priority=10):
	print "=================AddFirewallRule(添加规则Rule)=============="
	url='http://127.0.0.1:8080/firewall/rules/'+dp
	data={"nw_src":nw_src, "nw_dst": nw_dst, "nw_proto":nw_proto,"dp_dst":port,"actions":action,"priority":priority}
	
	req=urllib2.Request(url,json.dumps(data))
	response=urllib2.urlopen(req)
	res=response.read().encode('utf8')
	print res
#删除rule
def delete_rule(dp,ruleid):
	print "=================Delete(删除Rule)======================="
	url='http://127.0.0.1:8080/firewall/rules/'+dp
	values={"rule_id":ruleid}
	request=urllib2.Request(url,json.dumps(values))
	request.add_header('Content-Type', 'your/contenttype')
	request.get_method = lambda: 'DELETE'
	res= urllib2.urlopen(request)
	res_data=res.read().encode('utf8')
	print res_data
 
if __name__=='__main__':
	print "===================配置防火墙配置================================="
	data=look_firestat()#查看防火墙状态
	dp=data[0]['switch_id']#记录交换机id
	enable_firewall(dp) #使能防火墙
	look_firestat()
	rule_firewall(dp)
	print "=======================添加广播=================================="
	add_Brodcastrule(dp,"10.0.0.0/8","10.0.0.0/8")#添加广播，实现所有主机通信
	rule_firewall(dp)#显示Rules
	while(True):
		Cmd=raw_input("Add Or Delete Rule<input ADD or DEL>: ")
		if(Cmd=="ADD"):
			proto=raw_input("UDP OR TCP: ")
			port=raw_input("Port: ")
			source=raw_input("Source IP: ")
			des=raw_input("Destination IP: ")
			action=raw_input("ALLOW OR DENY: ")
			add_rule(dp,source,des,proto,port,action)
			print "======================ADD SUCCESS========================"
			Cmd2=raw_input("QUIT OR CONTINUE<Q OR C>: ")
			if(Cmd2=='Q'):
				break
			elif(Cmd2=='C'):
				continue
		elif(Cmd=="DEL"):
			rule_firewall(dp)
			num=raw_input("Input Rule-ID<int>: ")
			delete_rule(dp,num);
			print "======================DELETE SUCCESS====================="
			Cmd3=raw_input("QUIT OR CONTINUE<Q OR C>: ")
			if(Cmd3=='Q'):
				break
			elif(Cmd3=='C'):
				continue