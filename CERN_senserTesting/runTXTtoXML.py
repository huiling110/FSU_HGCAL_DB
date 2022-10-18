import TXT_TO_XML


def main():
    # i assume the FSU uses raw data which is in cern box
    # raw data: /eos/user/h/hgsensor/HGCAL_test_results/Results/Preseries_June2022/HPK_8in_444ch_300048/
    # data from analysis frame work in pclcd15: /home/data/hgsensor_iv/
    # /home/data/hgsensor_iv/Hamamatsu_Preseries_June2022
    # inputTxtDir = '/Users/hua/mountFolderForpcd/hgsensor_iv/Hamamatsu_Preseries_June2022/temperature_scaled/'
    inputTxtDir = '/eos/user/h/hgsensor/HGCAL_test_results/Results/Preseries_June2022/HPK_8in_444ch_300048/'
    inputFile = 'HPK_8in_444ch_300048_IV.txt'
    # inputTxtDir = '../'
    # inputFile = 'HPK_8in_198ch_2019_N4792_18_03242022_FullRetest_IV.txt'
    inputTxt = inputTxtDir + inputFile

    TXT_TO_XML.make_xml_schema_HGC_CERN_SENSOR_IV(inputTxt)


if __name__ == '__main__':
    main()
