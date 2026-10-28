# 2. Packet Tracer 네트워크 구축 및 PC 간 통신 실습

> Synced from Notion. Edit the source page in Notion; this file is generated.

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
