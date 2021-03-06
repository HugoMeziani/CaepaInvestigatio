import json
import mongoengine
from caepainvestigatio import connect
from caepainvestigatio.ORM import collect
from caepainvestigatio.logging_conf import initLogging

log = initLogging()

def JSONtoDB(files_list):
    """ browse and insert into mongoDB all json files """

    for json_file in files_list:
        with open(json_file) as data_file:
            # browse JSON files
            try:
                myJSON = json.load(data_file)
                log.debug(myJSON['hiddenService'])
            except:
                log.error(json_file+".ERREUR")
                return
        data = json.loads(myJSON.decode('utf-8', 'ignore'))
        send_db(data)


def send_db(data):
    """ send data collected to mongo db """

    # insert JSON files into mongoDB
    try:
        collect.Collect(**data).save()
    except mongoengine.NotUniqueError:
        col = collect.Collect.objects(hiddenService=data['hiddenService']).first()
        col.update(**data)
    #except:
    #    log.error('ERROR send to db')
