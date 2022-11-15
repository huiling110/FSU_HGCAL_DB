import subprocess

import TXT_TO_XML


def main():
    # raw data: /eos/user/h/hgsensor/HGCAL_test_results/Results/Preseries_June2022/HPK_8in_444ch_300048/
    # data from analysis frame work in pclcd15: /home/data/hgsensor_iv/
    # /home/data/hgsensor_iv/Hamamatsu_Preseries_June2022
    # inputTxtDir = '/Users/hua/mountFolderForpcd/hgsensor_iv/Hamamatsu_Preseries_June2022/temperature_scaled/'
    inputTxtDir = '/eos/user/h/hgsensor/HGCAL_test_results/Results/Preseries_June2022/HPK_8in_444ch_300048/'
    inputFile = 'HPK_8in_444ch_300048_IV.txt'
    # inputTxtDir = '../'
    # inputFile = 'HPK_8in_198ch_2019_N4792_18_03242022_FullRetest_IV.txt'
    inputTxt = inputTxtDir + inputFile

    user = 'Huiling'
    location = 'CERN'
    TXT_TO_XML.make_xml_schema_HGC_CERN_SENSOR_IV(inputTxt, location, user)
    


def uplodingToDB(xml):
    upCommand = 'scp {} USERNAME@dbloader-hgcal.cern.ch:/home/dbspool/spool/hgc/int2r/'.format(xml)
    subprocess.run( upCommand, shell=True)
    

if __name__ == '__main__':
    main()
