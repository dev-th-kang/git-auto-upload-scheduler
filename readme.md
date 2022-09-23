# git-auto uploader v1.0.0

*  프로젝트 폴더&파일
    ```
    │  .gitignore
    │  app.py
    │  autocommit.bat
    │  config.ini
    │  git-auto-upload.py
    │  README.md
    │  updateList.md
    │
    ├─autorun
    │      autoRun.py
    │
    ├─crawler
    │      gitCrawler.py
    │
    ├─data
    │      commitdata.json
    │      folderinfo.json
    │
    └─projectmanger
        folderManger.py
        projectModify.py
    
    ``` 


* ***위 프로그램을 만들게 된 이유***
    ```
    '1 day 1 commit' 을 원하는 사람들 중, 프로젝트에 전념하여, 그날 분량을 커밋을 하지 못하는 상황이 생기게 된다. 그래서 시간주기를 셋팅해서 매일 그 시간마다 자동으로 커밋이 올라가면 깃허브 커밋걱정을 안해도되서 편하지않을까해서 만들게 되었다.
    ```


* ***현재 개발중인 사항***😒
  * 프로젝트 폴더 관리자 기능을 추가함으로써, 폴더를 좀 더 유동적이게 확인할 수 있게하는 기능
  * commit된 데이터를 날짜별로 json 파일에 저장
  * 로그값 남기기, 제대로 구동이 되고있는지, 상태에 대한 로그 남기기
  * .git이 없는 파일 올릴 방법 고안하기

<br>

* ***현재 개발된 사항***😁
  * 자동으로 config.ini파일의 cycle값을 변경하면, 그 시간에 자동 업로드가 진행된다.
  * 또한 그냥 진행되는 것이 아니라, 작업하던 프로젝트(.git이 이미 있는 프로젝트) 가 마지막 commit된 정보와 다른지 판단해서 자동 업로드가 진행된다.
  * 설정해놓은 프로젝트 폴더에 수정여부에 따라 그 프로젝트가 전부 git push 된다. 
  * 그 날 이미 github에 커밋된 내용이 있으면, 이 프로그램이 굳이 진행되지않는다.



> 현재 git clone을 하거나 한 번이상 git push를 한 프로젝트가 아니라면, 프로젝트 폴더가 이 프로그램에서 적용이 되지않는다.

<br>
<br>
<br>

## 사용법
<hr>

* config.ini 에서 설정값을 수정한다.( ""(쌍따옴표)를 넣지않습니다. )
  ```
    [GIT_INFO]
    userName = username

    [AUTORUN_SETTING]
    timeCycle = 11:50
    ```
* 현재 프로젝트 폴더 리스트 셋팅도 자동화로 되어있지 않아서 초기에는 사용자가 셋팅을 해야합니다. 제일 우선적으로 개선될 사항이지만, 현재 버전에서는 지원하지않습니다.

    * data/folderinfo.json 파일을 수정합니다. file_path에는 절대경로를 넣어주고 앞에 오름차순으로 숫자 key값 넣어주셔야합니다.
        ```json
        {
            "folder": {
                "1": "file_path",
                "2": "file_path"
            }
        }
        ```
    
    이 이상 셋팅할 사항은 없습니다. 

   ** 위 프로그램은 OpenSource이며, 목적에 맞게끔 변경해서 사용하셔도 무관합니다.**