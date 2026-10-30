# 2. Packet Tracer 네트워크 구축 및 PC 간 통신 실습

> Synced from Notion. Edit the source page in Notion; this file is generated.

## 학습 목표

Router의 역할과 기본 게이트웨이의 필요성을 이해하고, 인터페이스 설정·라우팅 테이블 확인·정적 경로 설정·설정 저장의 기본 흐름을 익힌다.

## 개념 정리 — Router와 기본 게이트웨이

### 1. Router가 필요한 이유

- Switch는 일반적으로 같은 LAN 안에서 프레임을 전달하고, Router는 서로 다른 IP 네트워크 사이에서 패킷을 전달한다.

- PC가 목적지 IP를 자신의 네트워크 밖에 있다고 판단하면 패킷을 기본 게이트웨이로 보낸다.

- 기본 게이트웨이는 보통 해당 LAN에 연결된 Router 인터페이스의 IP 주소다. PC의 IP 주소·서브넷 마스크와 게이트웨이는 서로 맞는 네트워크로 설정해야 한다.

### 2. Router 인터페이스와 라우팅 테이블

- Router의 각 인터페이스에는 연결된 네트워크에 맞는 IP 주소와 서브넷 마스크를 설정한다.

- 인터페이스가 활성화되고 연결 상태가 정상이라면 Router는 해당 네트워크를 직접 연결된 경로로 라우팅 테이블에 등록한다.

- 다른 Router 뒤에 있는 네트워크는 정적 경로 등으로 알려줘야 한다. 정적 경로의 기본 형식은 다음과 같다.

```plain text
ip route <목적지 네트워크> <서브넷 마스크> <다음 홉 IP>
```

- 통신이 왕복하려면 요청이 가는 경로뿐 아니라 응답이 돌아오는 경로도 필요하다.

### 3. 설정·검증·저장 순서

1. 토폴로지와 각 장치의 IP 주소 계획을 확인한다.

1. Router 인터페이스에 IP 주소와 서브넷 마스크를 설정하고 `no shutdown`을 적용한다.

1. PC의 IP 주소·서브넷 마스크·기본 게이트웨이를 설정한다.

1. 필요한 정적 경로를 양방향으로 설정한다.

1. `show ip interface brief`, `show ip route`, `ping <목적지 IP>`로 상태와 경로를 확인한다.

1. Router에서 `copy running-config startup-config`로 설정을 저장하고, Packet Tracer 프로젝트도 별도로 `.pkt` 파일로 저장한다.

> 참고: 아래 하위 페이지의 IP 주소와 인터페이스 이름은 해당 실습 예시를 위한 값이다. 실제 수업 토폴로지에서 포트 이름이나 주소 계획이 다르면 현재 토폴로지에 맞춰 조정한다.

---

## 🧪 관련 실습

개념을 확인한 뒤 아래 실습을 진행한다. 각 실습의 상세 설정과 실제 통신 결과는 해당 하위 페이지에 기록한다.

[Host Route 설정](https://app.notion.com/p/409300052f66817d81eafc44fbfb4701)

- 핵심 내용: 스위치에 연결된 PC별 ping 결과와 Host Route(/32) 개념을 기록했다. 이미지에서는 PC0 통신은 성공, PC1 통신은 실패로 표시되어 있다.

### [단일 라우터를 이용한 네트워크 연결](https://www.notion.so/408300052f6681cc9324f93a88145866)

## 학습 목표

Router의 두 인터페이스를 서로 다른 IP 네트워크에 연결하고, PC의 Default Gateway를 설정해 통신을 확인한다.

## 주소 계획

| 장치/인터페이스 | IP Address | Subnet Mask | Default Gateway |
| --- | --- | --- | --- |
| PC1 | `192.168.10.1` | `255.255.255.0` | `192.168.10.254` |
| Router Fa0/0 | `192.168.10.254` | `255.255.255.0` | 해당 없음 |
| Router Fa0/1 | `192.168.20.254` | `255.255.255.0` | 해당 없음 |
| PC2 | `192.168.20.1` | `255.255.255.0` | `192.168.20.254` |

## Router 인터페이스 설정

장비 모델에 따라 인터페이스 이름이 다를 수 있으므로 실제 포트를 확인한다.

```plain text
enable
configure terminal
interface fa0/0
ip address 192.168.10.254 255.255.255.0
no shutdown
exit
interface fa0/1
ip address 192.168.20.254 255.255.255.0
no shutdown
end
```

## PC 설정 및 테스트

각 PC에서 **Desktop → IP Configuration**에 IP 주소, 마스크, 게이트웨이를 입력한다. PC1에서 실행한다.

```plain text
ping 192.168.20.1
```

## 검증 및 문제 해결

- `show ip interface brief`로 인터페이스 주소와 상태를 확인한다.

- PC의 Default Gateway가 연결된 Router 인터페이스 주소와 일치하는지 확인한다.

- 인터페이스가 비활성 상태라면 올바른 포트에서 `no shutdown`을 적용했는지 확인한다.

- 기본 게이트웨이와 라우팅 개념은 관련 개념 문서 및 수업 내용을 함께 참고한다.

- 핵심 내용: Router 인터페이스와 PC의 IP 설정, 기본 게이트웨이를 확인하고 한 대의 Router를 이용해 네트워크를 연결한다.

### [다중 라우터 연결 및 정적 라우팅 설정](https://www.notion.so/408300052f6681059ce2d01f0a80cb6b)

## 학습 목표

Serial 링크로 Router들을 연결하고, 직접 연결되지 않은 LAN에 도달할 정적 경로를 설정한다.

## 실습 A — Router 2대

```plain text
PC1 ── R0 ──(Serial)── R1 ── PC2
```

| 장치/인터페이스 | IP Address | Subnet Mask |
| --- | --- | --- |
| PC1 | `192.168.10.1` | `255.255.255.0` |
| R0 Fa0/0 | `192.168.10.254` | `255.255.255.0` |
| R0 Se0/0 | `1.1.1.1` | `255.0.0.0` |
| R1 Se0/0 | `1.1.1.2` | `255.0.0.0` |
| R1 Fa0/0 | `192.168.20.254` | `255.255.255.0` |
| PC2 | `192.168.20.1` | `255.255.255.0` |

R0에서 인터페이스 주소와 활성화를 설정한 뒤 원격 LAN 경로를 추가한다.

```plain text
ip route 192.168.20.0 255.255.255.0 1.1.1.2
```

R1에는 반대 방향 경로를 추가한다.

```plain text
ip route 192.168.10.0 255.255.255.0 1.1.1.1
```

PC1 게이트웨이는 `192.168.10.254`, PC2 게이트웨이는 `192.168.20.254`로 설정한다.

## 실습 B — Router 3대

```plain text
PC0 ── Router0 ──(Serial)── Router1 ──(Serial)── Router2 ── PC2
```

| 장치/인터페이스 | IP Address | Subnet Mask |
| --- | --- | --- |
| PC0 | `192.168.10.1` | `255.255.255.0` |
| Router0 Fa0/0 | `192.168.10.254` | `255.255.255.0` |
| Router0 Se0/0 | `1.1.1.1` | `255.0.0.0` |
| Router1 Se0/0 | `1.1.1.2` | `255.0.0.0` |
| Router1 Fa0/0 | `192.168.20.254` | `255.255.255.0` |
| PC1 | `192.168.20.1` | `255.255.255.0` |
| Router1 Se0/1 | `2.1.1.1` | `255.0.0.0` |
| Router2 Se0/1 | `2.1.1.2` | `255.0.0.0` |
| Router2 Fa0/0 | `192.168.30.254` | `255.255.255.0` |
| PC2 | `192.168.30.1` | `255.255.255.0` |

각 Router에서 LAN 인터페이스와 Serial 인터페이스에 IP 주소를 설정하고 `no shutdown`을 적용한다. 그 다음 직접 연결되지 않은 LAN으로 정적 경로를 설정한다.

- Router0: `192.168.20.0/24`, `192.168.30.0/24`의 다음 홉은 `1.1.1.2`

- Router1: `192.168.10.0/24`의 다음 홉은 `1.1.1.1`; `192.168.30.0/24`의 다음 홉은 `2.1.1.2`

- Router2: `192.168.10.0/24`, `192.168.20.0/24`의 다음 홉은 `2.1.1.1`

정적 경로 명령 형식은 다음과 같다.

```plain text
ip route <목적지 네트워크> <서브넷 마스크> <다음 홉 IP>
```

## 공통 검증

```plain text
show ip interface brief
show ip route
```

PC에서 원격 PC로 `ping`을 실행한다. Serial 링크가 `up/up`이 아니면 케이블, 포트, 주소, `no shutdown` 및 필요한 경우 DCE 측 clock 설정을 확인한다. 왕복 통신을 위해 양쪽 방향의 경로가 필요하다.

## 저장

Router에서 `copy running-config startup-config`를 실행하고, Packet Tracer 프로젝트도 별도로 `Ctrl+S` 또는 **File → Save**로 `.pkt` 파일에 저장한다.

## 관련 개념

- IPv4 주소와 서브넷 마스크는 [1. IPv4 주소 기초와 주소 유형](https://app.notion.com/p/406300052f66815a9458f782574e8dbc) 및 [3. 서브넷 마스크와 서브넷팅](https://app.notion.com/p/408300052f66814d8619ff8ccc2c30b4)을 참고한다.

- 핵심 내용: 여러 Router를 연결하고 정적 경로를 설정해 서로 다른 네트워크 간 통신을 구성한다.

## 공통 확인 명령어

```plain text
show ip interface brief
show ip route
ping <목적지 IP>
copy running-config startup-config
```

- 인터페이스 상태, IP 주소, 기본 게이트웨이, 정적 경로와 케이블을 순서대로 확인한다.

- Router 설정 저장과 Packet Tracer `.pkt` 프로젝트 저장은 별개다.

- 관련 개념은 [IPv4 주소 기초](https://app.notion.com/p/406300052f66815a9458f782574e8dbc)와 [서브넷팅](https://app.notion.com/p/408300052f66814d8619ff8ccc2c30b4) 페이지에서 확인한다.

실습별 주소와 설정은 실제 수업 토폴로지에 맞는지 확인하면서 사용한다.

## 복습 체크리스트

- [x] Switch와 Router가 담당하는 역할의 차이를 설명할 수 있다.

- [x] 기본 게이트웨이가 필요한 상황을 설명할 수 있다.

- [x] Router 인터페이스의 IP 주소와 서브넷 마스크를 설정하고 상태를 확인할 수 있다.

- [x] 직접 연결된 경로와 정적 경로의 차이를 구분할 수 있다.

- [x] `show ip interface brief`, `show ip route`, `ping`으로 연결과 경로를 확인할 수 있다.

- [x] Router 설정과 Packet Tracer 프로젝트 파일을 각각 저장해야 하는 이유를 설명할 수 있다.
