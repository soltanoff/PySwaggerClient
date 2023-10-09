import json

import six

from .comm import PrimJSONEncoder


class MimeCodec:
    def __init__(self):
        plainCodec = PlainCodec()
        jsonCodec = JsonCodec()
        htmlTextCodec = HtmlTextCodec()

        self._codecs = {}
        self.register('text/plain', plainCodec)
        self.register('application/json', jsonCodec)
        self.register('text/json', jsonCodec)
        self.register('text/html', htmlTextCodec)

    def register(self, mime, codec):
        self._codecs[mime.lower()] = codec

    def unregister(self, mime):
        self._codecs.pop(mime.lower())

    def codec(self, mime):
        mime = mime.split(';', 1)[0]
        mime = mime.strip().lower()
        return self._codecs.get(mime, None)

    def marshal(self, mime, value, **kwargs):
        codec = self.codec(mime)
        if not codec:
            raise Exception('Could not find codec for %s, value: %s, args: %s' % (mime, value, kwargs))
        return codec.marshal(value, **kwargs)

    def unmarshal(self, mime, data, **kwargs):
        codec = self.codec(mime)
        if not codec:
            raise Exception('Could not find codec for %s, data: %s, args: %s' % (mime, data, kwargs))
        return codec.unmarshal(data, **kwargs)


class PlainCodec:
    def marshal(self, value, **kwargs):
        return value

    def unmarshal(self, data, **kwargs):
        return data


class JsonCodec:
    def marshal(self, value, **kwargs):
        return json.dumps(value, cls=PrimJSONEncoder)

    def unmarshal(self, data, **kwargs):
        if isinstance(data, six.binary_type):
            data = data.decode('utf-8')
        return json.loads(data)


class HtmlTextCodec:
    def marshal(self, value, **kwargs):
        try:
            return json.dumps(value, cls=PrimJSONEncoder)
        except:
            return str(value).encode('utf-8')

    def unmarshal(self, data, **kwargs):
        if isinstance(data, six.binary_type):
            decoded_data = data.decode('utf-8')
        else:
            decoded_data = data

        try:
            return json.loads(decoded_data)
        except:
            return decoded_data
