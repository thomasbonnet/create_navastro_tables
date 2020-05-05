import logging
import os

from table_dieumegard import TableDieumegard


logger = logging.getLogger()

logger.info("Creating tables")

table_dieumegard = TableDieumegard()
rootfilename = "dieumegard"
filename = "{}.tex".format(rootfilename)
outfile = open(filename, mode="w", encoding="utf8")
outfile.write(table_dieumegard.build())
outfile.close()

command = 'pdflatex {}'.format(filename)
os.system(command)
logger.info("finished")
# os.remove(filename)

for file in ["{}.log".format(rootfilename), "{}.aux".format(rootfilename)]:
    if os.path.isfile(file):
        os.remove(file)
