# 옵저버 패턴

## 1. 정의

객체간의 연결에서 객체의 상태 변화를 관찰하는 Observer, 그리고 자신의 옵저버들에게 메서드 등을 통해서 상태 변화를 통지하는 Observable(Subject)을 사용하는 디자인 패턴이다.

이벤트 기반 프로그래밍, MVC 패턴 등에서 자주 이용된다.

---

## 2. 작동원리

+ 그림

---

### Observer 객체는 다음과 같이 구성된다.

- notify()

notifyObservers() 를 통해 호출되며, 관찰 대상의 변화에 따라서 특정 동작을 수행한다.

---

### Observable 객체는 다음과 같이 구성된다.

- observerCollection

자신의 옵저버들의 목록

- registerObserver(observer)

자신의 observerCollection에 observer를 등록하는 메서드

- unregisterobserver(observer)

자신의 observerCollection에서 observer를 제거하는 메서드

- notifyObservers()

옵저버블의 상태가 변화되면 observerCollection의 옵저버들에게 상태가 변했음을 알려주는 메서드

---

## 3. MVC 패턴과 옵저버 패턴

+ 그림

MVC 패턴에서는 Model은 원칙적으로 데이터를 저장, 수정하는 역할만 해야한다.

하지만 사용자는 View를 통해 Model의 상태 변화를 즉각적으로 알 수 있어야 하므로, 어쩔 수 없이 Model에 자신의 상태변화를 View에게 알리는 기능이 있어야 한다.

직접 Model 객체가 View 객체에게 상태변화를 알리는 방식을 사용할 수도 있지만,

옵저버 패턴을 사용하여 Model - View 사이를 느슨하게 연결할 수 있다.

Model - View 사이에 옵저버 패턴을 사용하게 된다면 다음과 같은 장점들이 있다.

1. 객체간의 의존성을 줄일 수 있다.
2. 의존성을 줄인다는 것은 훗날 유지보수할 떄 있어서 작업하게 될 코드의 양이 대폭 줄어들게 된다는 것을 의미한다.
3. 다른 뷰(옵저버) 가 생겨났을 때 기존 코드를 수정하지 않아도 된다.

프로젝트의 유지보수 측면에서 옵저버 패턴을 사용하는 것이 좋다는 것을 알아보았다.

## 4. 참고
https://ko.wikipedia.org/wiki/옵저버_패턴

http://dynaticy.tistory.com/entry/DesignPattern-2-Observer-Pattern에-대한-고민