from django.test import TestCase

# Create your tests here.
from django.http import HttpRequest,HttpResponse
from django.http import JsonResponse
from json import dumps
from django.core import serializers
from ailb import models
from ailb.service.indexService import indexService


def get_stats():

    indexServiceIn = indexService()
    tps = indexServiceIn.searchReply(6)
    print(tps[0].replyDetail)

    print(serializers.serialize('json', tps))