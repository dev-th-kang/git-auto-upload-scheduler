# git-auto-upload-scheduler

> 업무에 집중하며, 당일 작업한양을 커밋을 못할 경우를 대비해서 수정되거나 만들어진 프로젝트가 있다면, 자동으로 커밋!


## plan

* 2022-09-16
  * 일정시간 (오후 11시45분으로 예상) 시 코드실행
    * **[func1](./gitcrawler/crawler.py)** - beautifulsoup4의 crawling기능을 통해서 사용자의 당일 커밋여부 확인

    * **[func2](./fmanagement/checkfolder.py)** - 프로젝트 진행 중인 폴더에서 수정된 내용이 있는지 확인(python 모듈을 활용할지, git diff 기능을 활용할지는 미정)


    * func1, func2가 만족한다면, upload 기능 실행
      * 최초 실행 시, 깃허브 로그인 요구됨
      * git push 작업 수행
  
  * 현재 func1 1차 제작완료
 
* 2022-09-17 
    * bat 파일로 자동으로 되는지 실험
    * 프로젝트 폴더 데이터 저장 bat파일로 인자값 넘길 수 있는지 체크 해봐야함
    * 폴더목록을 json 형태로 저장 
    * 각 기능별로 분리, 폴더 분리


