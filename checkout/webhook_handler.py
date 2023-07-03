from django.http import HttpResponse


class StripeWH_Handler:
    """ Handle strip webhooks """

    def __init(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
