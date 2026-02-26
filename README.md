# KERNEL: K8s Evidence Reconstruction &amp; Network Event Ledger

<img src="./image/thumbNail.png"/>

> 본 프로젝트는 토스뱅크 사이버보안 엔지니어 부트캠프에서 진행되었습니다.

## 프로젝트 Intro
KERNEL 프로젝트는 쿠버네티스 환경에서 위협 행위에 대한 **탐지 및 분석 고도화**라는 주제로 진행한 팀 프로젝트입니다. </br>**eBPF** 기반 **CNI**인 **Cilium**과 시스템 및 네트워크 탐지 도구인 **Tetragon**과 **Hubble**을 활용함으로서 User Level에서의 부하를 최소화하고 **다중 탐지 프레임워크** 설계를 통해 탐지 Hole을 최소화하는 것을 목표로 했습니다.</br>
또한 탐지된 시스템, 네트워크 이벤트를 **상관분석**하여 공격 시나리오를 재구성하는 것을 목표로 했습니다.

## 팀 소개
<div align="center">
<h3>Team ForenSeek</h3>

| **조성열** | **한희수** | **엄민송** | **황주하** | **이주현** | **허창렬** |
| :------: | :------: | :------: | :------: | :------: | :------: |
| [<img src="https://github.com/Choseongyul.png" height=150 width=150> <br/> @sychoii](https://github.com/Choseongyul) | [<img src="https://github.com/crowndaisy76.png" height=150 width=150> <br/> @crowndaisy](https://github.com/crowndaisy76) | [<img src="https://github.com/skymin1121.png" height=150 width=150> <br/> @skymin1121](https://github.com/skymin1121) | [<img src="https://github.com/jjjjjuha.png" height=150 width=150> <br/> @jjjjjuha](https://github.com/jjjjjuha) | [<img src="https://github.com/ImitationProgramer.png" height=150 width=150> <br/> @ImitationProgramer](https://github.com/ImitationProgramer) | [<img src="https://github.com/loopbackIP.png" height=150 width=150> <br/> @CHANGRYEOL HEO](https://github.com/loopbackIP) |
| **팀장** | **팀원** | **팀원** | **팀원** | **팀원** | **팀원** |
| **공격 시나리오 설계</br>Tetragon 정책 설계</br>탐지 프로세스 고도화** | **Click House 분석 파이프라인 설계</br>탐지 및 분석 프로세스 고도화** | **다중 탐지 프레임워크 설계</br>탐지 및 분석 프로세스 고도화** | **인프라 설계</br>Sigma Rule 최적화** | **인프라 설계</br>Sigma Rule 최적화** | **공격 시나리오 설계</br>Sigma Rule 최적화** |
</div>

## 프로젝트 기술 스택
<div align="center">

![Kubernetes](https://img.shields.io/badge/KUBERNETES-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white) 
![Vagrant](https://img.shields.io/badge/VAGRANT-1868F2?style=for-the-badge&logo=vagrant&logoColor=white) 
![VMware](https://img.shields.io/badge/VMWARE-607078?style=for-the-badge&logo=vmware&logoColor=white) </br>
![Cilium](https://img.shields.io/badge/CILIUM-FFBF00?style=for-the-badge&logo=cilium&logoColor=black)
<img src="https://tetragon.io/images/tetragon-shield.png" height="28" /> ![TETRAGON](https://img.shields.io/badge/-TETRAGON-FFBF00?style=for-the-badge&logoColor=black) 
<img src="https://cilium.io/static/hubble-dark-1-91890e273cb3d50a8f520e3cbe178806.svg" height="28" /> ![HUBBLE](https://img.shields.io/badge/-HUBBLE-FFBF00?style=for-the-badge) </br>
![OpenSearch](https://img.shields.io/badge/OPENSEARCH-005EB8?style=for-the-badge&logo=opensearch&logoColor=white)
![ClickHouse](https://img.shields.io/badge/CLICKHOUSE-FFCC01?style=for-the-badge&logo=clickhouse&logoColor=black)
![Python](https://img.shields.io/badge/PYTHON-3776AB?style=for-the-badge&logo=python&logoColor=white)
<img src="https://images.squarespace-cdn.com/content/v1/5ab952d7506fbeaa1f512f11/1586076420678-9G5MBZOQJLH0WXKP42V3/5bfdce88cd3820f7c5c21e02_mitre.png?format=1500w" height="28" /> ![MITRE ATT&CK](https://img.shields.io/badge/-MITRE_ATT%26CK-E02424?style=for-the-badge&logoColor=black)
<img src="https://sigmahq.io/images/logo.svg" height="28" /> ![SIGMA](https://img.shields.io/badge/-SIGMA-3D4D65?style=for-the-badge&logoColor=white)

</div>