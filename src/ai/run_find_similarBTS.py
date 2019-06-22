# -*- coding: utf-8 -*-
#############################################
#     openface 컨테이너를 통해              #
#     가장 닮은 BTS 멤버를 찾아             #
#     텍스트 파일에 결과를 출력해주는 코드  #
#############################################

import subprocess

# 사용자의 사진을 도커로 cp
subprocess.call(['docker cp TEST/test.jpg openface:/root/openface/input/bts_input/test.jpg'], shell=True)

# openface 컨테이너 실행
subprocess.call(['docker start openface'], shell=True)

# 닮은 BTS 멤버 찾기
res = subprocess.check_output(['docker exec -it openface /bin/bash find_similarBTS.sh'],universal_newlines=True,shell=True)

# 원하는 res 포맷으로 변경
res = res.split("if diff:\n")
res_name, res_acq = res[1].split()

# 텍스트 파일에 결과 출력
f = open("result_bts.txt", "w")
f.write("당신은 " + str(float(res_acq)*100)+ "%의 확률로 " +res_name+ "을 닮았습니다!\n")
f.close()
