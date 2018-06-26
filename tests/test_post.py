import pytest
import sys
import os.path
src_code_path = str(os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir))))+"/src/utils/"
sys.path.append(src_code_path)
from post import Post 



def test_post_1():
	req = {
			"title": "How to use virtualenv with Python?",
			"body":'''
			<p>I am planning to install a virtual environment for Python in order to keep my Python packages separate. One of the motivations for this is also to have two versions of Python on my machine (Ubuntu 14.04) co-existing. I have the following wonders:</p>
			<ol>
			<li>In what order should Python, PIP and virtualenv be installed? Does it matter at all?</li>
			<li>Once done, how can I keep two python versions separate under virtualenv?</li>
			<li>Assume I am working on separate projects, is it recommended to keep each of the project in a separate folder created by virtualenv or not?</li>
			</ol>

			<p>I would like to know experts opinion in order to do things in the right manner and wisely.</p>
	    	''',
	    	"tags":["python","virtualenv"],
	    	"hour":17,
	    	"day":5

	    }


	correct_title="How to use virtualenv with Python?"
	body='''I am planning to install a virtual environment for Python in order to keep my Python packages separate. One of the motivations for this is also to have two versions of Python on my machine (Ubuntu 14.04) co-existing. I have the following wonders:
		 In what order should Python, PIP and virtualenv be installed? Does it matter at all?
		 Once done, how can I keep two python versions separate under virtualenv?
		 Assume I am working on separate projects, is it recommended to keep each of the project in a separate folder created by virtualenv or not?
		 I would like to know experts opinion in order to do things in the right manner and wisely.
		 '''

	correct_body=body.replace("\n","").replace("\t","") 
	post=Post(req)

	assert(post.body.replace(" ","")==correct_body.replace(" ",""))
	assert(post.title==correct_title)
	assert(len(post.tags)==2)
	assert(post.hour==17)
	assert(post.day==5)
	assert(len(post.code)==0)
	assert(len(post.url)==0)



def test_post_2():
	req = {
			"title": "during docker build, add-apt-repository returns “keyserver receive failed: No name”",
			"body":'''
					<p>I am trying to build a Docker image for building Zoo-Project, following <a href="http://www.zoo-project.org/docs/install/debian.html" rel="nofollow noreferrer">installation guidelines</a>.</p>

					<p>I am behind a company proxy, so I set up environnement to point to it :</p>

					<pre><code>root@myContainer$ env
					HTTP_PROXY=http://10.xxx.y.zzz:3128
					https_proxy=http://10.xxx.y.zzz:3128
					http_proxy=http://10.xxx.y.zzz:3128
					HTTPS_PROXY=http://10.xxx.y.zzz:3128
					</code></pre>

					<p>Unfortunately, when I try to run the following command from the Dockerfile or from within the container, it keeps failing :</p>

					<pre><code>root@myContainer$ add-apt-repository ppa:ubuntugis/ppa
					 Official stable UbuntuGIS packages.
					 More info: https://launchpad.net/~ubuntugis/+archive/ubuntu/ppa
					Press [ENTER] to continue or ctrl-c to cancel adding it
					gpg: keybox '/tmp/tmpl5mo2xz1/pubring.gpg' created
					gpg: keyserver receive failed: No name
					</code></pre>

					<p>I tried the following with no success : </p>

					<ul>
					<li>apt-key adv --keyserver keys.gnupg.net --recv-keys 226213AA  : <em>keyserver receive failed: No name</em></li>
					<li>apt-key adv --keyserver.ubuntu.com --recv-keys 226213AA : <em>keyserver receive failed: No name</em></li>
					<li>the same with url replaced by ip address (91.189.90.55, 18.191.65.131) : <em>keyserver receive failed: No keyserver available</em></li>
					</ul>

					<p>My resolv.conf looks like this (from within the container):</p>

					<pre><code>root@myContainer$  more /etc/resolv.conf 
					# Dynamic resolv.conf(5) file for glibc resolver(3) generated by resolvconf(8)
					#     DO NOT EDIT THIS FILE BY HAND -- YOUR CHANGES WILL BE OVERWRITTEN
					nameserver 8.8.8.8
					nameserver 8.8.8.4
					nameserver 10.171.108.2
					search rennes.mycompany.fr
					</code></pre>

					<p>Anyone has a tip here?</p>
            ''',
	    	"tags":["docker","proxy","dns","apt"],
	    	"hour":17,
	    	"day":5

	    }


	correct_title="during docker build, add-apt-repository returns “keyserver receive failed: No name”"
	body='''
		I am trying to build a Docker image for building Zoo-Project, following .

		I am behind a company proxy, so I set up environnement to point to it :
		Unfortunately, when I try to run the following command from the Dockerfile or from within the container, it keeps failing :

		I tried the following with no success :

		apt-key adv --keyserver keys.gnupg.net --recv-keys 226213AA : keyserver receive failed: No name
		apt-key adv --keyserver.ubuntu.com --recv-keys 226213AA : keyserver receive failed: No name
		the same with url replaced by ip address (91.189.90.55, 18.191.65.131) : keyserver receive failed: No keyserver available
		My resolv.conf looks like this (from within the container):
		Anyone has a tip here?
		'''

	correct_body=body.replace("\n","").replace("\t","") 
	post=Post(req)

	assert(post.body.replace(" ","")==correct_body.replace(" ",""))
	assert(post.title==correct_title)
	assert(len(post.tags)==4)
	assert(post.hour==17)
	assert(post.day==5)
	assert(len(post.code)==3)
	assert(len(post.url)==1)


		    