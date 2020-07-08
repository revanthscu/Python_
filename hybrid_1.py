class P1:pass
class P2: pass
class C(P2,P2):pass
print(C.mro())
