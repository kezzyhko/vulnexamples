FROM python:3.6.4
RUN mkdir /bot
WORKDIR /bot
COPY . /bot/
RUN pip3 install selenium==3.141.0

ENV PHANTOMJS_VERSION 2.1.1
ENV PHANTOMJS_PLATFORM linux-x86_64

RUN wget -q -O /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-${PHANTOMJS_VERSION}-${PHANTOMJS_PLATFORM}.tar.bz2 && \
  tar -xjf /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 -C /tmp && \
  rm -f /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \
  mv /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64/ /usr/local/share/phantomjs && \
  ln -s /usr/local/share/phantomjs/bin/phantomjs /usr/local/bin/phantomjs