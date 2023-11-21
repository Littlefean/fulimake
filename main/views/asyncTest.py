import asyncio

from django.http import JsonResponse
from django.views import View


class AsyncView(View):
    async def get(self, request):
        await asyncio.sleep(1)
        return JsonResponse({
            'text': 'success'
        })
