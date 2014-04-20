pilani-pirates
==============

Indexing and searching site for BITS Pilani LAN sharing


# Setting up

1. Install the dependencies

    ```bash
    $ sudo apt-get update
    $ sudo apt-get install build-essential python-dev libpcre3 libpcre3-dev default-jre git python-pip curl nginx
    ```

2. Create a virtualenv and activate it
3. Install required python packages

    ```bash
    $ pip install -r requirements.txt
    ```

4. Install Apache Solr (for search)

    ```bash
    $ cd ~
    $ mkdir pilani-pirates
    $ cd pilani-pirates
    $ curl -O https://archive.apache.org/dist/lucene/solr/4.7.1/solr-4.7.1.tgz
    $ tar xvzf solr-4.7.1.tgz
    ```

5. Clone this repo

    ```bash
    $ cd ~/pilani-pirates
    $ git clone https://github.com/aps-sids/pilani-pirates.git
    $ cd pilani-pirates
    ```

6. Edit `pilani_pirates.ini` and `pirate_site_nginx.conf` as per your system
7. Create database,collect the static files and build solr schema

    ```bash
    $ python pilani_pirates/manage.py syncdb
    $ python pilani_pirates/manage.py collectstatic
    $ python pilani_pirates/manage.py build_solr_schema > schema.xml
    ```
This will create a file `schema.xml`. Move this file to `~/pilani-pirates/solr-4.7.1/example/solr/collection1/conf/` and replace the existing `schema.xml`.
8. Setup nginx

    ```bash
    # Symlink pirate_site_nginx.conf file from /etc/nginx/sites-enabled so nginx can see it
    $ sudo ln -s ~/pilani-pirates/pilani-pirates/pirate_site_nginx.conf /etc/nginx/sites-enabled/
    $ sudo /etc/init.d/nginx start    # start or restart nginx
    ```

# Running

1. Start the solr server

    ```bash
    $ cd ~/pilani-pirates/solr-4.7.1/example/
    $ java -jar start.jar
    ```

2. Build the search indexes and start uWSGI webserver in a new terminal (from activated virtualenv)

    ```bash
    $ cd ~/pilani-pirates/pilani-pirates/
    $ python pilani_pirates/manage.py rebuild_index
    $ uwsgi pilani_pirates.ini
    ```
