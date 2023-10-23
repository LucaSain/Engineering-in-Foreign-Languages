### 1 
Prove that 
1) K is a vector space over itself, with addition and multiplication in K;
	a) (K,+) abelian group (K=field)
	b) let  x form K , a,b from K; from a) => (a+b)x=ax+bx
	c) let v,w from K, a from K, (v+w)a = va + wa
	d) let a,b from K, v from K, (ab)v = a(bv), v-vector
	e) It exists 1k in K; let v from K, 1kv=v
	**=>** k is a vector space over itself, "+,multiplication"

2) K^3 is a vector space, where K^3 = {(x1,x2,x3)|x1,x2,x3 from K}is endowed with:
	1) (x1,x2,x3)+(y1,y2,y3)=(x1+y1,x2+y2,x3+y3)
	2) a(x1,x2,x3)=(ax1,ax2,ax3)
	a) (K^3,+)=abelian group
	b) Let v from K^3; a,b form K such that (a+b)v ?= av+bv
		(a+b)v = (a+b)(x1,x2,x3)=((a+b)x1,(a+b)x2,(a+b)x3) (o1)
		av + bv = (ax1,ax2,ax3)+(bx1,bx2,bx3) = ((a+b)x1,(a+b)x2,(a+b)x3) 
		= (o2)
	c) Let v1,v2 from K^3 and a from K => (v1+v2)a = v1a + v2a
		(v1+v2)a = (x1+y1,x2+y2,x3+y3)a = (a(x1+y1),a(x2+y2),a(x3+y3))=
		= (ax1,ax2,ax3)+(ay1,ay2,ay3)
	d) Whatever a,b from K, whatever v from K^3: (ab)v = a(bv)
		(ab)v=(abx1,abx2,abx3) (o1) 
		a(bx1,bx2,bx3)=(abx1,abx2,abx3) (o2)
		o1=o2 True
	e) It exists 1k from K, whatever v from K^3:
		1kv = v
		okv = ov = (ok,ok,ok)

3) M3(K) is vector space, endowed w/ addition and multiplication by scalars form K
	a) (M3(K),+) is abelian group
	b) let A from M3(K) and a,b from K - scalars => (a+b)A = aA+bA
	c) let A,B from M3(K) and a from K => (A+B)a = 

### 2
Let v be a real vector space. We denote by CV the set of formal combinations of type v+iw, where i=√-1
Show that CV is a complex vector space, with the following operations:
	Whatever v + iw from C, v1+iw1 and whatever a = a+ib from C
	(v+iw) + (v1+iw1) =def= (v+v1,i(w+w1))
	a(v+iw) =def= (av,iaw)
	a) CV = abelian group
	b) z from CV,  a,b from C => (a+b)z = az+bz
		(a+b)z=(a+b)(v+wi)=(a+b)v+(a+b)wi=av+bv+awi+bwi= a(v+wi)+b(v+wi)=az+bz
	c) let z1,z2 from CV and a from C such that (z1+z2)a=z1a+z2a
	...
	d) let a,b from C and z from CV such that (ab)z=a(bz):
	<=> (ab)(v+wi) = a(b((v+wi))) <=> (abv,iabw)=a(bv,+)