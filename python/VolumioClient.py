#!/usr/bin/env python2

from socketIO_client import SocketIO, LoggingNamespace
#from socketIO_client import SocketIO

# Class for connecting to Volumio
class VolumioClient(object):
    def __init__(self, host="localhost", port=3000):
        self._host = host
        self._port = port
        self._status = ''
        self._title = ''
        self._artist = ''
        self._socketio = ''
        self._status_change_callback = ''
        self._title_change_callback = ''
        self._artist_change_callback = ''

    def on_status_change(self, callback):
        self._status_change_callback = callback

    def on_title_change(self, callback):
        self._title_change_callback = callback

    def on_artist_change(self, callback):
        self._artist_change_callback = callback

    # Callback function as response on 'getState', used to retrieve status, title, artist
    def on_push_state(self, *args):
    #    print('getstate', args)
        new_status = args[0]['status']
        if new_status != self._status:
            if self._status_change_callback:
                self._status_change_callback(new_status)
            self._status = new_status
        new_title = args[0]['title']
        if new_title != self._title:
            if self._title_change_callback:
                self._title_change_callback(new_title)
            self._title = new_title
        new_artist = args[0]['artist']
        if new_artist != self._artist:
            if self._artist_change_callback:
                self._artist_change_callback(new_artist)
            self._artist = new_artist

    def connect(self):
        self._socketio = SocketIO(self._host, self._port, LoggingNamespace)

        # getState response handler
        self._socketio.on('pushState', self.on_push_state)
        # getState command
        self._socketio.emit('getState')

    def wait(self):
    	self._socketio.wait()

if __name__ == "__main__":
    import sys

    status = 'unknown'

    # Define callback functions
    def status_changed(new_status):
	global status
        print('status_changed() status: ' +  status + '->' + new_status)
        status = new_status

    def title_changed(title):
        print('title_changed(): ' + title)

    def artist_changed(artist):
        print('artist_changed(): ' + artist)

    try:
        volumio = VolumioClient(host="localhost", port=3000)
        volumio.on_status_change(status_changed)
        volumio.on_title_change(title_changed)
        volumio.on_artist_change(artist_changed)
        volumio.connect()

        while True:
        	volumio.wait()

    except (KeyboardInterrupt, SystemExit):
        print("Keyboard or system exit interrupt");
        sys.exit();

    # Catch all other non-exit errors
    except Exception as e:
        print(e)
        sys.exit(1)

    except:
        sys.exit(0)


