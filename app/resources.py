from flask_restful import Resource
from flask import request, Response

from . import extensions
from . import db_mappings
from xml.etree.ElementTree import ElementTree, Element, SubElement, tostring



class Ping(Resource):
    def get(self):
        return "pong"


class Sitemap(Resource):
    def get(self):
        r = Response(sitemap_builder(), mimetype='text/xml')
        r.headers["Content-Type"] = "text/xml; charset=utf-8"
        return r



def sitemap_builder():
    
    urlset = Element('urlset')
    urlset.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')
    for u in get_urls():
        url = SubElement(urlset,'url')
        loc = SubElement(url, 'loc')
        lastmod = SubElement(url, 'lastmod')
        # no se si conviene poner la de hoy aca
        lastmod.text = "2017-06-10"
        loc.text = 'https://articulos.vivisaludable.com/' + u

    stiemap = u'<?xml version="1.0" encoding="UTF-8"?>\n'.encode('utf8') + tostring(urlset, encoding='utf-8')
    return stiemap
    
def get_urls():
    try:
        targetKeywordMappingFromUrl = db_mappings.TargetKeywords().fromUrl    
        queryResult = extensions.db.session.query(targetKeywordMappingFromUrl).all()
        allkw = [a_url[0] for a_url in queryResult]
        return allkw
    except Exception, e:
        raise e
    


extensions.api.add_resource(Ping, '/ping')
extensions.api.add_resource(Sitemap, '/sitemap')








