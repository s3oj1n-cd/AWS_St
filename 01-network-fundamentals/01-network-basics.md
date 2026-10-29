# 1. 네트워크 기초 & Packet Tracer 실습

> Synced from Notion. Edit the source page in Notion; this file is generated.

이 문서는 학습 목차입니다. 상세 설명은 각 하위 페이지에서 관리합니다.

# 네트워크 기초 학습 허브

이 페이지는 IPv4 기초 개념, Cisco Packet Tracer 실습, 서브넷팅 계산을 순서대로 학습하기 위한 목차다.

## 하위 페이지

### [1. IPv4 주소 기초와 주소 유형](02-ipv4-subnet-mask.md)

## 학습 목표

IPv4 주소의 구조와 표현 방법, 주소 클래스, 통신 방식, 특수 주소, 사설 IP와 공인 IP를 이해한다. 서브넷을 실제로 계산하고 나누는 내용은 3번 페이지에서 학습한다.

## 1. IPv4 주소의 기본 구조

- IPv4 주소는 점으로 구분된 10진수 네 구간으로 표현한다. 예: `192.168.1.10`

- 각 구간(옥텟)은 8bit이며, 전체 길이는 `8bit × 4 = 32bit`다.

- 8bit 값의 범위는 `00000000`(0)부터 `11111111`(255)까지다.

- 각 비트의 값은 왼쪽부터 `128, 64, 32, 16, 8, 4, 2, 1`이다.

### 2진수와 10진수 변환 예시

| 2진수 | 10진수 |
| --- | --- |
| `11000000` | 192 |
| `11100000` | 224 |
| `11110000` | 240 |
| `11111000` | 248 |

## 2. IPv4 클래스와 기본 서브넷 마스크

클래스 기반 주소 지정(Classful Addressing)은 IP 주소의 첫 번째 옥텟을 기준으로 주소 범위를 구분하는 방식이다. 아래의 기본 마스크는 클래스 기반 학습을 위한 값이다.

| 클래스 | 첫 번째 옥텟 범위 | 기본 서브넷 마스크 | CIDR |
| --- | --- | --- | --- |
| A | 1–126 | `255.0.0.0` | `/8` |
| B | 128–191 | `255.255.0.0` | `/16` |
| C | 192–223 | `255.255.255.0` | `/24` |
| D | 224–239 | 멀티캐스트용 | 해당 없음 |
| E | 240–255 | 실험 및 연구용으로 구분 | 해당 없음 |

- `127.0.0.1`은 자기 자신을 가리키는 Loopback 주소의 대표 예시다.

- D Class는 멀티캐스트 주소에 사용된다. 원문 예시에는 `224.0.0.9`가 RIPv4 관련 멀티캐스트 주소로 적혀 있다.

- 실제 네트워크에서는 클래스보다 CIDR 프리픽스와 서브넷 마스크를 기준으로 네트워크를 구분하는 경우가 일반적이다.

## 3. IPv4 통신 방식

| 방식 | 의미 | 설명 |
| --- | --- | --- |
| Unicast | 1:1 | 한 송신자가 특정 수신자 한 대에 데이터를 전송한다. |
| Multicast | 1:Group | 한 송신자가 특정 그룹에 데이터를 전송한다. |
| Broadcast | 1:All | 한 네트워크의 브로드캐스트 범위에 있는 대상에게 데이터를 전송한다. |

### Broadcast 예시

- `255.255.255.255`: 제한된 브로드캐스트 주소로, 일반적으로 라우터를 넘어 전달되지 않는다.

- Directed Broadcast는 특정 네트워크의 브로드캐스트 주소를 가리킨다. 원문에서는 `1.255.255.255`를 `1.0.0.0` 네트워크의 예시로 제시한다.

브로드캐스트 범위는 주소와 서브넷 마스크에 따라 달라진다.

## 4. 사설 IP와 공인 IP

### 사설 IP(Private IP)

사설 IP는 내부 네트워크에서 사용하며, 인터넷에서 직접 라우팅되지 않는다. 내부 기기가 인터넷에 접속할 때는 일반적으로 NAT를 통해 공인 IP로 변환한다.

| 사설 IPv4 범위 | 전체 범위 | 흔한 사용 예 |
| --- | --- | --- |
| 10.0.0.0/8 | `10.0.0.0 – 10.255.255.255` | 기업 내부 네트워크 |
| 172.16.0.0/12 | `172.16.0.0 – 172.31.255.255` | 사무실·조직 내부 네트워크 |
| 192.168.0.0/16 | `192.168.0.0 – 192.168.255.255` | 가정용 네트워크 |

### 공인 IP(Public IP)

- 인터넷에서 전역적으로 라우팅할 수 있도록 관리되는 주소다.

- 일반적으로 ISP 또는 네트워크 사업자를 통해 할당받는다.

- IPv4 주소 자원의 한계는 IPv6 전환을 추진하는 배경 중 하나다.

## 5. 네트워크가 같은 경우와 다른 경우

- 같은 IP 네트워크에 속한 PC는 일반적으로 같은 LAN의 Hub 또는 Switch를 통해 직접 통신할 수 있다.

- 서로 다른 IP 네트워크 사이의 통신에는 일반적으로 Router와 같은 Layer 3 장비가 필요하다.

- PC의 IP 주소만 보지 말고, 설정된 서브넷 마스크까지 함께 확인해야 한다.

구체적인 서브넷 마스크의 AND 연산, 네트워크 주소·브로드캐스트 주소 계산, 서브넷 분할은 [3. 서브넷 마스크와 서브넷팅](https://app.notion.com/p/408300052f66814d8619ff8ccc2c30b4) 페이지에서 학습한다.

## 핵심 요약

- IPv4는 32bit이며, 8bit씩 네 옥텟으로 표현한다.

- A/B/C 클래스의 기본 마스크는 각각 `/8`, `/16`, `/24`다.

- Unicast는 1:1, Multicast는 1:Group, Broadcast는 1:All 통신이다.

- 사설 IP는 내부 네트워크에서 사용하며, 공인 IP는 인터넷에서 라우팅할 수 있다.

- 같은 네트워크인지 판단할 때는 IP 주소와 서브넷 마스크를 함께 본다.

## 관련 학습 페이지

[3. 서브넷 마스크와 서브넷팅](https://app.notion.com/p/408300052f66814d8619ff8ccc2c30b4)

[2. Packet Tracer 네트워크 구축 및 PC 간 통신 실습](https://app.notion.com/p/406300052f668160abb8c6b633382c3b)

### [2. Packet Tracer 네트워크 구축 및 PC 간 통신 실습](../02-cisco-packet-tracer/01-pc-to-pc-communication.md)

## 학습 목표와 전체 순서

이 페이지는 Packet Tracer에서 PC와 네트워크 장비를 연결하고, Router 수를 늘려 가며 통신을 구성하는 실습 노트다. 아래 순서대로 진행한다.

1. 장비와 케이블 이해하기

1. 실습 A — 같은 네트워크의 PC끼리 통신하기

1. 실습 B — Router 한 대로 서로 다른 네트워크 연결하기

1. 실습 C — Router 두 대를 Serial로 연결하고 정적 경로 설정하기

1. 실습 D — Router 세 대를 직렬로 연결하고 정적 경로 설정하기

1. 통신 확인 및 문제 해결

1. 설정과 Packet Tracer 파일 저장

## 1. 장비 역할과 케이블 연결

### 장비 역할

- **PC**: IP 주소와 서브넷 마스크를 설정해 데이터를 송수신한다.

- **Hub**: 들어온 신호를 다른 포트로 전달하는 장비로, 일반적으로 OSI 1계층으로 설명한다.

- **Switch**: MAC 주소를 이용해 같은 LAN 안에서 프레임을 전달하는 장비로, 일반적으로 OSI 2계층이다.

- **Router**: 서로 다른 IP 네트워크 사이에서 패킷을 전달하는 장비로, 일반적으로 OSI 3계층이다.

### 케이블 선택 — 수업에서 배운 기준

이 실습에서는 수업에서 배운 규칙을 기준으로 케이블을 선택한다.

- **실선: Copper Straight-Through**

  - PC ↔ Switch

  - PC ↔ Hub

  - Router ↔ Switch

  - Router ↔ Hub

- **점선: Copper Cross-Over**

  - Hub ↔ Switch

  - PC ↔ Router

Packet Tracer에서 자동 연결 기능을 사용할 수도 있다. 실제 케이블 선택은 장비 포트와 Auto-MDI/MDIX 지원 여부에 따라 달라질 수 있으므로, 실습이나 시험에서는 수업에서 안내한 기준을 따른다.

## 2. 실습 A — 같은 네트워크의 PC끼리 통신하기

### 구성

PC 두 대를 Hub 또는 Switch에 연결한다.

```plain text
PC1 ──┐
      ├── Switch 또는 Hub
PC2 ──┘
```

### IP 주소 설정

각 PC에서 **Desktop → IP Configuration**을 열고 다음 값을 입력한다.

| 장치 | IP Address | Subnet Mask |
| --- | --- | --- |
| PC1 | `192.168.1.10` | `255.255.255.0` |
| PC2 | `192.168.1.20` | `255.255.255.0` |

두 PC는 모두 `192.168.1.0/24` 네트워크에 속하므로 같은 LAN 안에서 직접 통신할 수 있다. 이 실습에서는 PC 간 통신에 Default Gateway가 필요하지 않다.

### 통신 테스트

PC1에서 **Desktop → Command Prompt**를 열고 다음을 실행한다.

```plain text
ping 192.168.1.20
```

응답이 오면 같은 네트워크의 PC 간 통신이 성공한 것이다.

## 3. 실습 B — Router 한 대로 서로 다른 네트워크 연결하기

서로 다른 IP 네트워크 사이의 통신에는 Router가 필요하다. 각 PC의 Default Gateway는 PC와 같은 서브넷에 연결된 Router 인터페이스 주소로 설정한다.

### 주소 계획

| 장치/인터페이스 | IP Address | Subnet Mask | Default Gateway |
| --- | --- | --- | --- |
| PC1 | `192.168.10.1` | `255.255.255.0` | `192.168.10.254` |
| Router Fa0/0 | `192.168.10.254` | `255.255.255.0` | 해당 없음 |
| Router Fa0/1 | `192.168.20.254` | `255.255.255.0` | 해당 없음 |
| PC2 | `192.168.20.1` | `255.255.255.0` | `192.168.20.254` |

### Router 인터페이스 설정

Router의 **CLI** 탭에서 다음 명령어를 순서대로 입력한다. `Router>` 같은 프롬프트는 현재 모드를 표시하므로, 실제 입력 시에는 프롬프트 뒤의 명령어만 입력한다.

```plain text
Router> enable
Router# configure terminal
Router(config)# interface fa0/0
Router(config-if)# ip address 192.168.10.254 255.255.255.0
Router(config-if)# no shutdown
Router(config-if)# exit
Router(config)# interface fa0/1
Router(config-if)# ip address 192.168.20.254 255.255.255.0
Router(config-if)# no shutdown
Router(config-if)# end
Router#
```

### PC 설정 및 테스트

각 PC의 **Desktop → IP Configuration**에서 위 표의 IP 주소, 서브넷 마스크, Default Gateway를 입력한다. 그런 다음 PC1에서 다음 명령어로 확인한다.

```plain text
ping 192.168.20.1
```

### CLI 모드 빠른 정리

- `Router>`: 사용자 EXEC 모드. `enable`로 관리자 모드에 진입한다.

- `Router#`: 관리자 EXEC 모드. 확인 명령어를 실행하거나 `configure terminal`로 설정 모드에 진입한다.

- `Router(config)#`: 전역 설정 모드. `interface`와 `ip route` 등을 입력한다.

- `Router(config-if)#`: 인터페이스 설정 모드. `ip address`와 `no shutdown` 등을 입력한다.

- `exit`: 이전 설정 모드로 나간다.

- `end`: 설정 모드를 종료하고 `Router#`로 돌아간다.

인터페이스 이름은 Router 모델에 따라 다를 수 있으므로 실제 연결된 포트를 확인한다.

## 4. 실습 C — Router 두 대를 Serial로 연결하기

Router R0와 R1을 Serial 링크로 연결한다. 각 Router는 자신에게 직접 연결되지 않은 상대편 LAN으로 가는 정적 경로(Static Route)를 알아야 한다.

### 토폴로지와 주소 계획

```plain text
PC1 ── R0 ──(Serial)── R1 ── PC2
```

| 장치/인터페이스 | IP Address | Subnet Mask | 역할 |
| --- | --- | --- | --- |
| PC1 | `192.168.10.1` | `255.255.255.0` | R0 쪽 PC |
| R0 Fa0/0 | `192.168.10.254` | `255.255.255.0` | PC1의 Gateway |
| R0 Se0/0 | `1.1.1.1` | `255.0.0.0` | Serial 링크 |
| R1 Se0/0 | `1.1.1.2` | `255.0.0.0` | Serial 링크 |
| R1 Fa0/0 | `192.168.20.254` | `255.255.255.0` | PC2의 Gateway |
| PC2 | `192.168.20.1` | `255.255.255.0` | R1 쪽 PC |

### R0 설정

```plain text
Router> enable
Router# configure terminal
Router(config)# interface fa0/0
Router(config-if)# ip address 192.168.10.254 255.255.255.0
Router(config-if)# no shutdown
Router(config-if)# exit
Router(config)# interface se0/0
Router(config-if)# ip address 1.1.1.1 255.0.0.0
Router(config-if)# no shutdown
Router(config-if)# exit
Router(config)# ip route 192.168.20.0 255.255.255.0 1.1.1.2
Router(config)# end
Router#
```

### R1 설정

```plain text
Router> enable
Router# configure terminal
Router(config)# interface fa0/0
Router(config-if)# ip address 192.168.20.254 255.255.255.0
Router(config-if)# no shutdown
Router(config-if)# exit
Router(config)# interface se0/0
Router(config-if)# ip address 1.1.1.2 255.0.0.0
Router(config-if)# no shutdown
Router(config-if)# exit
Router(config)# ip route 192.168.10.0 255.255.255.0 1.1.1.1
Router(config)# end
Router#
```

### PC 설정 및 테스트

- PC1: IP `192.168.10.1`, Mask `255.255.255.0`, Gateway `192.168.10.254`

- PC2: IP `192.168.20.1`, Mask `255.255.255.0`, Gateway `192.168.20.254`

PC1에서 `ping 192.168.20.1`을, PC2에서 `ping 192.168.10.1`을 실행한다. 양쪽 Router에 정적 경로가 있어야 왕복 통신이 가능하다.

## 5. 실습 D — Router 세 대를 Serial로 직렬 연결하기

Router0–Router1–Router2를 직렬 연결하고, 세 LAN의 PC가 서로 통신하도록 구성한다. Router마다 인터페이스 주소를 설정하고, 직접 연결되지 않은 LAN으로 가는 정적 경로를 추가한다.

### 토폴로지와 주소 계획

```plain text
PC0 ── Router0 ──(Serial)── Router1 ──(Serial)── Router2 ── PC2
```

| 장치/인터페이스 | IP Address | Subnet Mask | 역할 |
| --- | --- | --- | --- |
| PC0 | `192.168.10.1` | `255.255.255.0` | Router0 쪽 PC |
| Router0 Fa0/0 | `192.168.10.254` | `255.255.255.0` | PC0 Gateway |
| Router0 Se0/0 | `1.1.1.1` | `255.0.0.0` | Router0–Router1 |
| Router1 Se0/0 | `1.1.1.2` | `255.0.0.0` | Router0–Router1 |
| Router1 Fa0/0 | `192.168.20.254` | `255.255.255.0` | PC1 Gateway |
| PC1 | `192.168.20.1` | `255.255.255.0` | Router1 쪽 PC |
| Router1 Se0/1 | `2.1.1.1` | `255.0.0.0` | Router1–Router2 |
| Router2 Se0/1 | `2.1.1.2` | `255.0.0.0` | Router1–Router2 |
| Router2 Fa0/0 | `192.168.30.254` | `255.255.255.0` | PC2 Gateway |
| PC2 | `192.168.30.1` | `255.255.255.0` | Router2 쪽 PC |

### Router0 설정

```plain text
Router> enable
Router# configure terminal
Router(config)# interface fa0/0
Router(config-if)# ip address 192.168.10.254 255.255.255.0
Router(config-if)# no shutdown
Router(config-if)# exit
Router(config)# interface se0/0
Router(config-if)# ip address 1.1.1.1 255.0.0.0
Router(config-if)# no shutdown
Router(config-if)# exit
Router(config)# ip route 192.168.20.0 255.255.255.0 1.1.1.2
Router(config)# ip route 192.168.30.0 255.255.255.0 1.1.1.2
Router(config)# end
Router#
```

### Router1 설정

```plain text
Router> enable
Router# configure terminal
Router(config)# interface fa0/0
Router(config-if)# ip address 192.168.20.254 255.255.255.0
Router(config-if)# no shutdown
Router(config-if)# exit
Router(config)# interface se0/0
Router(config-if)# ip address 1.1.1.2 255.0.0.0
Router(config-if)# no shutdown
Router(config-if)# exit
Router(config)# interface se0/1
Router(config-if)# ip address 2.1.1.1 255.0.0.0
Router(config-if)# no shutdown
Router(config-if)# exit
Router(config)# ip route 192.168.10.0 255.255.255.0 1.1.1.1
Router(config)# ip route 192.168.30.0 255.255.255.0 2.1.1.2
Router(config)# end
Router#
```

### Router2 설정

```plain text
Router> enable
Router# configure terminal
Router(config)# interface fa0/0
Router(config-if)# ip address 192.168.30.254 255.255.255.0
Router(config-if)# no shutdown
Router(config-if)# exit
Router(config)# interface se0/1
Router(config-if)# ip address 2.1.1.2 255.0.0.0
Router(config-if)# no shutdown
Router(config-if)# exit
Router(config)# ip route 192.168.10.0 255.255.255.0 2.1.1.1
Router(config)# ip route 192.168.20.0 255.255.255.0 2.1.1.1
Router(config)# end
Router#
```

### PC 설정 및 테스트

- PC0: IP `192.168.10.1`, Mask `255.255.255.0`, Gateway `192.168.10.254`

- PC1: IP `192.168.20.1`, Mask `255.255.255.0`, Gateway `192.168.20.254`

- PC2: IP `192.168.30.1`, Mask `255.255.255.0`, Gateway `192.168.30.254`

PC0에서 `ping 192.168.20.1`과 `ping 192.168.30.1`을 실행한다. PC2에서는 `ping 192.168.10.1`과 `ping 192.168.20.1`을 실행한다.

이미지에는 Router0의 `ip route 2.0.0.0 255.0.0.0 1.1.1.2`, Router2의 `ip route 1.0.0.0 255.0.0.0 2.1.1.1`도 표시되어 있었다. 이 두 경로는 각각 /8 대역 전체를 대상으로 한다. 세 LAN 사이의 통신만을 위한 기본 구성에는 위에서 설정한 구체적인 원격 LAN 경로면 충분하다. 수업에서 이미지의 추가 경로를 요구하면 별도로 입력한다.

## 6. 공통 확인 및 문제 해결

각 Router에서 관리자 EXEC 모드인 `Router#`에서 다음 명령어를 실행한다.

```plain text
Router# show ip interface brief
Router# show ip route
```

- `show ip interface brief`: 인터페이스 IP 주소와 상태를 확인한다.

- `show ip route`: 직접 연결된 네트워크(`C`)와 정적 경로(`S`)를 확인한다.

- Serial 링크가 `up/up`이 아니면 케이블, 연결 포트, IP 주소와 인터페이스 활성화 여부를 확인한다. DCE 쪽에서 클록 설정이 필요한 경우 해당 인터페이스에 지원되는 `clock rate` 값을 설정한다.

통신이 되지 않으면 다음 순서로 확인한다.

1. 케이블이 올바른 장비와 포트에 연결되어 있는가?

1. PC와 Router의 IP 주소 및 서브넷 마스크가 올바른가?

1. 각 PC의 Default Gateway가 해당 LAN의 Router 인터페이스 주소와 일치하는가?

1. Router 인터페이스에 IP 주소가 설정되어 있고 `no shutdown`이 적용되어 있는가?

1. 각 Router의 정적 경로가 목적지 LAN과 다음 홉 주소에 맞게 설정되어 있는가?

1. ping 대상 IP 주소가 정확한가? 첫 ping이 실패하면 ARP 확인 과정일 수 있으므로 잠시 후 다시 실행한다.

### IP 주소와 서브넷 마스크

네트워크는 IP 주소만이 아니라 IP 주소와 서브넷 마스크를 함께 보고 구분한다. 예를 들어 `192.10.10.1/24`과 `192.0.0.1/24`은 서로 다른 네트워크다. Hub 또는 일반적인 Layer 2 Switch만으로는 서로 다른 IP 네트워크 사이를 라우팅할 수 없다.

## 7. 설정과 실습 파일 저장

Router CLI에서 관리자 EXEC 모드인 `Router#`에서 설정을 저장한다.

```plain text
Router# copy running-config startup-config
```

저장 확인 메시지가 나오면 Enter를 누른다. 지원되는 장비에서는 `write memory`를 사용할 수도 있다.

Packet Tracer 프로젝트 파일은 별도로 **File → Save** 또는 **Ctrl+S**를 눌러 `.pkt` 파일로 저장한다. Router 설정 저장과 Packet Tracer 프로젝트 저장은 서로 다른 작업이므로 둘 다 수행한다.

## 실습 파일

- `Same_net.pkt` — 파일명상 같은 네트워크 실습 파일

- `Dif_net.pkt` — 파일명상 서로 다른 네트워크 실습 파일

파일명으로 실습 유형을 구분했으며, 파일 내부의 실제 토폴로지와 설정값은 여기서 확인하지 못했다. 위의 주소들은 절차 설명용 예시이므로 실제 파일에 설정된 값과 다를 수 있다.

### [3. 서브넷 마스크와 서브넷팅](https://www.notion.so/408300052f66814d8619ff8ccc2c30b4)

이 페이지는 서브넷 마스크와 서브넷팅 계산에 집중한다. IPv4 주소 구조, 클래스, 통신 방식, 사설/공인 IP는 [1. IPv4 주소 기초와 주소 유형](https://app.notion.com/p/406300052f66815a9458f782574e8dbc) 페이지를 참고한다.

## 1. 서브넷 마스크의 역할

서브넷 마스크는 IPv4 주소에서 네트워크 부분과 호스트 부분을 구분하는 32비트 값이다.

- 마스크의 비트 `1`은 네트워크 부분을 나타낸다.

- 마스크의 비트 `0`은 호스트 부분을 나타낸다.

- CIDR 표기 `/26`은 앞의 26bit가 네트워크 부분이라는 뜻이다.

## 2. AND 연산으로 네트워크 주소 구하기

IP 주소와 서브넷 마스크를 비트 단위 AND 연산하면 네트워크 주소를 구할 수 있다. AND 연산은 두 비트가 모두 1일 때만 결과가 1이다.

| A | B | A AND B |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

### 예제

IP 주소 `192.168.10.65`, 서브넷 마스크 `255.255.255.192` (`/26`)를 사용한다.

마지막 옥텟만 2진수로 바꾸면 다음과 같다.

- IP 주소의 마지막 옥텟: `65 = 01000001`

- 마스크의 마지막 옥텟: `192 = 11000000`

- AND 결과: `01000000 = 64`

따라서 네트워크 주소는 `192.168.10.64`다.

## 3. 서브넷팅이란?

서브넷팅(Subnetting)은 하나의 네트워크를 여러 개의 작은 네트워크로 나누는 기술이다. 주소를 효율적으로 배분하고 네트워크를 관리하기 쉽게 하는 데 사용한다.

## 4. 서브넷 개수로 나누기 — /24를 네 개의 /26으로 분할

예제에서는 `192.168.10.0/24` 네트워크를 `255.255.255.192` (`/26`) 마스크로 4개 서브넷으로 나눈다.

- 원래 네트워크: `192.168.10.0/24`

- 새 서브넷 마스크: `255.255.255.192`

- CIDR: `/26`

- 마지막 옥텟의 블록 크기: `256 - 192 = 64`

- 서브넷 개수: 4개

- 각 서브넷의 전체 주소 수: 64개

- 각 서브넷에서 일반적으로 할당 가능한 호스트 주소 수: `2^6 - 2 = 62`

| 서브넷 | 네트워크 주소 | 사용 가능한 호스트 주소 | 브로드캐스트 주소 |
| --- | --- | --- | --- |
| 1 | `192.168.10.0` | `192.168.10.1 – 192.168.10.62` | `192.168.10.63` |
| 2 | `192.168.10.64` | `192.168.10.65 – 192.168.10.126` | `192.168.10.127` |
| 3 | `192.168.10.128` | `192.168.10.129 – 192.168.10.190` | `192.168.10.191` |
| 4 | `192.168.10.192` | `192.168.10.193 – 192.168.10.254` | `192.168.10.255` |

## 5. 계산 순서 정리

1. IP 주소와 서브넷 마스크를 확인한다.

1. CIDR 프리픽스에서 네트워크 비트 수를 확인한다.

1. 필요한 경우 블록 크기를 계산한다. 해당 옥텟의 블록 크기는 `256 - 마스크 옥텟 값`이다.

1. 블록 크기 단위로 네트워크 주소를 찾는다.

1. 다음 네트워크 주소 바로 전 주소를 브로드캐스트 주소로 찾는다.

1. 네트워크 주소와 브로드캐스트 주소 사이의 주소를 일반적인 사용 가능 호스트 주소로 확인한다.

## 복습 체크리스트

- [ ] 서브넷 마스크에서 네트워크 비트와 호스트 비트를 구분할 수 있다.

- [ ] IP 주소와 마스크의 AND 연산으로 네트워크 주소를 구할 수 있다.

- [ ] `/24`를 네 개의 `/26` 서브넷으로 나눌 수 있다.

- [ ] `/26`의 블록 크기가 64이고 일반적인 사용 가능 호스트 주소가 62개인 이유를 설명할 수 있다.

## 관련 학습 페이지

[1. IPv4 주소 기초와 주소 유형](https://app.notion.com/p/406300052f66815a9458f782574e8dbc)

[2. Packet Tracer 네트워크 구축 및 PC 간 통신 실습](https://app.notion.com/p/406300052f668160abb8c6b633382c3b)

## 추천 학습 순서

1. **IPv4 기초** — IP 주소 구조, 주소 유형, 사설/공인 IP 이해하기

1. **Packet Tracer 기초 실습** — PC를 Hub/Switch에 연결하고 ping 테스트하기

1. **서브넷팅** — AND 연산으로 네트워크 주소를 구하고 서브넷을 나누기

1. **Router 1대 실습** — 서로 다른 IP 네트워크를 연결하고 Default Gateway 설정하기

1. **Router 2대 이상 실습** — Serial 링크와 정적 경로 설정하기

1. **검증과 저장** — `ping`, `show ip interface brief`, `show ip route`로 확인하고 `copy running-config startup-config` 및 Packet Tracer `.pkt` 파일 저장하기

## 실습 시 유의사항

- 실습의 실제 IP 주소, 인터페이스 이름, 케이블 연결은 현재 Packet Tracer 토폴로지와 수업 지시를 기준으로 확인한다.

- Router의 running-config 저장과 Packet Tracer 프로젝트 파일 저장은 별개이므로 둘 다 수행한다.
