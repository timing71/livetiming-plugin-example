from livetiming.racing import Stat
from livetiming.service import BaseService, JSONFetcher


# URLs passed to fetchers must be bytes, not strings.
DATA_SOURCE_URL = b'http://ip.jsontest.com/'


# The service class MUST be called Service.
# BaseService is a useful point to inherit from since it implements a bunch of
# basic things for us.
# Note: you don't run this module directly. To start your service, make sure
# it's on your PYTHONPATH (i.e. run `pip install -e .`` from the project root)
# and run:
# $ livetiming-service -v example
class Service(BaseService):

    # With auto_poll set to True (default), we will have getRaceState called
    # every pollInterval seconds and automatically have the state published.
    # With auto_poll set to False we can control when we publish a state
    # update ourselves (e.g. immediately after we have received new data).
    auto_poll = False

    # Give attribution to your data source! Name and optional URL.
    attribution = ['Some Great Data Source', 'https://www.example.com/']

    def __init__(self, args, extra_args):
        super().__init__(args, extra_args)

        # Do any pre-run setup here, including setting up any initial state and
        # recurring data fetching.

        # JSONFetcher is a utility class that will poll the source URL every
        # pollInterval seconds, parse it to JSON, then call a callback method
        # with the parsed object.
        self._fetcher = JSONFetcher(
            DATA_SOURCE_URL,
            self._handle_data,
            self.getPollInterval()
        )

    # There are a bunch of stub methods you must implement to be a valid
    # service.  If any of the values used in the service manifest can change, be
    # sure to call publishManifest() to update the published manifest.

    def getName(self):
        return 'Example'

    # The description can be overridden on the commandline, or defaults to the
    # value returned here.
    def getDefaultDescription(self):
        return 'Just a test'

    def getVersion(self):
        return '0.0.1'

    def getPollInterval(self):
        return 10  # in seconds

    def getColumnSpec(self):
        # Define the columns available for the timing screen. You don't need to
        # restrict yourself to the predefined ones, but they should be used when
        # available.
        return [
            Stat.NUM,
            Stat.STATE,
            Stat.DRIVER,
            Stat.LAST_LAP,
            Stat.BEST_LAP
        ]

    def getTrackDataSpec(self):
        # For things like track/air temperature etc. - this should be a list
        # of headings.
        return []

    def start(self):
        # If you need to start any fetchers or connect to upstream, this is
        # the place to do so.

        self._fetcher.start()

        # The super call will not return (until the service is shut down).
        super().start()

    def _handle_data(self, data):
        self.log.info('Received data {data}', data=data)
        # do whatever we need to with the data we've been given, then:
        self._updateAndPublishRaceState()

    def getRaceState(self):
        # The big one!
        # Do whatever you need to do in order to return an object with the
        # following shape:
        return {
            'cars': [],
            'session': {
            }
        }
