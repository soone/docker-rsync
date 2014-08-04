FROM centos:update

ADD rsyncd.conf /etc/rsyncd.conf
RUN chmod 600 /etc/rsyncd.conf
ADD rsyncd.server.pas /etc/rsyncd.server.pas
RUN chmod 600 /etc/rsyncd.server.pas

RUN /etc/init.d/sshd start
RUN echo 'root:y123456passwd'|chpasswd

ADD server.sh /root/server.sh

EXPOSE 873 22

VOLUME ["/data"]

CMD ["/bin/bash", "/root/server.sh"]
