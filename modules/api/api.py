import requests
import chess
import logging
import re
import time
import pymongo
from modules.bcolors.bcolors import bcolors

def get_pgn():
    logging.debug(bcolors.WARNING + "Getting new game..." + bcolors.ENDC)
    client = pymongo.MongoClient("localhost", 27017)
    db = client.variantpuzzlegenerator
    item = db.unprocessed.find().limit(1)[0]

    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO

    io = StringIO(item["pgn"])

    db.unprocessed.remove({ "_id": item["_id"] })

    return io


def post_puzzle(cookies, puzzle):
    logging.info(bcolors.OKBLUE + str(puzzle.to_dict()) + bcolors.ENDC)
    success = False
    while not success:
        try:
            r = requests.post("https://chessvariants.training/Puzzle/Generation/Submit",
                cookies=cookies,
                data=puzzle.to_dict(),
                headers={"Origin": "https://chessvariants.training", "Referer": "https://chessvariants.training"})
            success = True
        except requests.ConnectionError:
            logging.warning(bcolors.WARNING + "CONNECTION ERROR: Failed to post puzzle.")
            logging.debug("Trying again in 30 sec" + bcolors.ENDC)
            time.sleep(30)
        except requests.SSLError:
            logging.warning(bcolors.WARNING + "SSL ERROR: Failed to post puzzle.")
            logging.debug("Trying again in 30 sec" + bcolors.ENDC)
            time.sleep(30)

        j = r.json()
        if j["success"]:
            logging.info(bcolors.WARNING + "Imported with ID " + str(j["id"]) + bcolors.ENDC)
        else:
            logging.error(bcolors.FAIL + "Failed to import with response: " + j["error"] + bcolors.ENDC)

