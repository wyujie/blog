Ubuntu下Salt Stack总结
----------------------
**安装:** 
<pre>sudo add-apt-repository ppa:saltstack/salt
sudo apt-get update
sudo apt-get install salt-master
sudo apt-get install salt-minion</pre>

<br/>
**Master配置:**

    配置文件路径 ==> /etc/salt/master.d/
    #在相应目录下新建文件(任意名字)
    #以下配置各个环境State的路径
    file_roots:
      #base环境必须存在(其实有例外,但是没必要折腾)
      base:	#base环境以及拥有的State路径(缩进是必须的)
        - /srv/salt/base
      dev:  #dev环境以及拥有的State路径(缩进是必须的)
        - /srv/salt/dev
      qa:	#qa环境以及拥有的State路径(缩进是必须的)
        - /srv/salt/qa
      prod:	#prod环境以及拥有的State路径(缩进是必须的)
        - /srv/salt/prod


<br/>
**Minion配置:**

    配置文件路径 ==> /etc/salt/minion.d/
    #在相应目录下新建文件(任意名字)
    添加 ==> master: yourserverip #换成master的IP
