# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import deserialize
from twilio import values
from twilio.instance_resource import InstanceResource
from twilio.list_resource import ListResource
from twilio.page import Page


class MobileList(ListResource):

    def __init__(self, version, account_sid, country_code):
        """
        Initialize the MobileList
        
        :param Version version: Version that contains the resource
        :param account_sid: A 34 character string that uniquely identifies this resource.
        :param country_code: The country_code
        
        :returns: MobileList
        :rtype: MobileList
        """
        super(MobileList, self).__init__(version)
        
        # Path Solution
        self._solution = {
            'account_sid': account_sid,
            'country_code': country_code,
        }
        self._uri = '/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code}/Mobile.json'.format(**self._solution)

    def stream(self, area_code=values.unset, contains=values.unset,
               sms_enabled=values.unset, mms_enabled=values.unset,
               voice_enabled=values.unset,
               exclude_all_address_required=values.unset,
               exclude_local_address_required=values.unset,
               exclude_foreign_address_required=values.unset, beta=values.unset,
               limit=None, page_size=None):
        """
        Streams MobileInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param unicode area_code: The area_code
        :param unicode contains: The contains
        :param bool sms_enabled: The sms_enabled
        :param bool mms_enabled: The mms_enabled
        :param bool voice_enabled: The voice_enabled
        :param bool exclude_all_address_required: The exclude_all_address_required
        :param bool exclude_local_address_required: The exclude_local_address_required
        :param bool exclude_foreign_address_required: The exclude_foreign_address_required
        :param bool beta: The beta
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)
        
        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        limits = self._version.read_limits(limit, page_size)
        
        page = self.page(
            area_code=area_code,
            contains=contains,
            sms_enabled=sms_enabled,
            mms_enabled=mms_enabled,
            voice_enabled=voice_enabled,
            exclude_all_address_required=exclude_all_address_required,
            exclude_local_address_required=exclude_local_address_required,
            exclude_foreign_address_required=exclude_foreign_address_required,
            beta=beta,
            page_size=limits['page_size'],
        )
        
        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, area_code=values.unset, contains=values.unset,
             sms_enabled=values.unset, mms_enabled=values.unset,
             voice_enabled=values.unset, exclude_all_address_required=values.unset,
             exclude_local_address_required=values.unset,
             exclude_foreign_address_required=values.unset, beta=values.unset,
             limit=None, page_size=None):
        """
        Lists MobileInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param unicode area_code: The area_code
        :param unicode contains: The contains
        :param bool sms_enabled: The sms_enabled
        :param bool mms_enabled: The mms_enabled
        :param bool voice_enabled: The voice_enabled
        :param bool exclude_all_address_required: The exclude_all_address_required
        :param bool exclude_local_address_required: The exclude_local_address_required
        :param bool exclude_foreign_address_required: The exclude_foreign_address_required
        :param bool beta: The beta
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)
        
        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        return list(self.stream(
            area_code=area_code,
            contains=contains,
            sms_enabled=sms_enabled,
            mms_enabled=mms_enabled,
            voice_enabled=voice_enabled,
            exclude_all_address_required=exclude_all_address_required,
            exclude_local_address_required=exclude_local_address_required,
            exclude_foreign_address_required=exclude_foreign_address_required,
            beta=beta,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, area_code=values.unset, contains=values.unset,
             sms_enabled=values.unset, mms_enabled=values.unset,
             voice_enabled=values.unset, exclude_all_address_required=values.unset,
             exclude_local_address_required=values.unset,
             exclude_foreign_address_required=values.unset, beta=values.unset,
             page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of MobileInstance records from the API.
        Request is executed immediately
        
        :param unicode area_code: The area_code
        :param unicode contains: The contains
        :param bool sms_enabled: The sms_enabled
        :param bool mms_enabled: The mms_enabled
        :param bool voice_enabled: The voice_enabled
        :param bool exclude_all_address_required: The exclude_all_address_required
        :param bool exclude_local_address_required: The exclude_local_address_required
        :param bool exclude_foreign_address_required: The exclude_foreign_address_required
        :param bool beta: The beta
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50
        
        :returns: Page of MobileInstance
        :rtype: Page
        """
        params = values.of({
            'AreaCode': area_code,
            'Contains': contains,
            'SmsEnabled': sms_enabled,
            'MmsEnabled': mms_enabled,
            'VoiceEnabled': voice_enabled,
            'ExcludeAllAddressRequired': exclude_all_address_required,
            'ExcludeLocalAddressRequired': exclude_local_address_required,
            'ExcludeForeignAddressRequired': exclude_foreign_address_required,
            'Beta': beta,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        
        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )
        
        return MobilePage(self._version, response, self._solution)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.MobileList>'


class MobilePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the MobilePage
        
        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: A 34 character string that uniquely identifies this resource.
        :param country_code: The country_code
        
        :returns: MobilePage
        :rtype: MobilePage
        """
        super(MobilePage, self).__init__(version, response)
        
        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of MobileInstance
        
        :param dict payload: Payload response from the API
        
        :returns: MobileInstance
        :rtype: MobileInstance
        """
        return MobileInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            country_code=self._solution['country_code'],
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.MobilePage>'


class MobileInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, country_code):
        """
        Initialize the MobileInstance
        
        :returns: MobileInstance
        :rtype: MobileInstance
        """
        super(MobileInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'friendly_name': payload['friendly_name'],
            'phone_number': payload['phone_number'],
            'lata': payload['lata'],
            'rate_center': payload['rate_center'],
            'latitude': deserialize.decimal(payload['latitude']),
            'longitude': deserialize.decimal(payload['longitude']),
            'region': payload['region'],
            'postal_code': payload['postal_code'],
            'iso_country': payload['iso_country'],
            'address_requirements': payload['address_requirements'],
            'beta': payload['beta'],
            'capabilities': payload['capabilities'],
        }
        
        # Context
        self._context = None
        self._solution = {
            'account_sid': account_sid,
            'country_code': country_code,
        }

    @property
    def friendly_name(self):
        """
        :returns: The friendly_name
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def phone_number(self):
        """
        :returns: The phone_number
        :rtype: unicode
        """
        return self._properties['phone_number']

    @property
    def lata(self):
        """
        :returns: The lata
        :rtype: unicode
        """
        return self._properties['lata']

    @property
    def rate_center(self):
        """
        :returns: The rate_center
        :rtype: unicode
        """
        return self._properties['rate_center']

    @property
    def latitude(self):
        """
        :returns: The latitude
        :rtype: unicode
        """
        return self._properties['latitude']

    @property
    def longitude(self):
        """
        :returns: The longitude
        :rtype: unicode
        """
        return self._properties['longitude']

    @property
    def region(self):
        """
        :returns: The region
        :rtype: unicode
        """
        return self._properties['region']

    @property
    def postal_code(self):
        """
        :returns: The postal_code
        :rtype: unicode
        """
        return self._properties['postal_code']

    @property
    def iso_country(self):
        """
        :returns: The iso_country
        :rtype: unicode
        """
        return self._properties['iso_country']

    @property
    def address_requirements(self):
        """
        :returns: The address_requirements
        :rtype: unicode
        """
        return self._properties['address_requirements']

    @property
    def beta(self):
        """
        :returns: The beta
        :rtype: bool
        """
        return self._properties['beta']

    @property
    def capabilities(self):
        """
        :returns: The capabilities
        :rtype: unicode
        """
        return self._properties['capabilities']

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.MobileInstance>'
