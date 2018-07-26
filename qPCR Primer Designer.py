print("Paste FASTA sequence, then hit 'enter'...")

fastaSL=[]
while True:
    fasta=input()
    fastaSL.append(fasta)
    if fasta=='':
        break

gene=''.join(fastaSL)

size=int(input('Primer length:\n'))
GCmax=int(input('Max GC%:\n'))
GCmin=int(input('Min GC%:\n'))

seq=[]
base=[]

for i in range(0,len(gene)-size+1):
    fragS=str(gene[i:i+size])
    seq.append(fragS)
    base.append(i)

for j in range(0,len(seq)):
    GC=[]
    frag=seq[j]
    loc=base[j]
    GCcount=[]
    for i in range(0,len(frag)):
        if frag[i]=='G':
            GCcount.append(i)
        if frag[i]=='C':
            GCcount.append(i)
    if GCmax > 100 * len(GCcount) / len(frag) > GCmin:
        GC.append((100*len(GCcount))//len(frag))
        rc=frag[::-1]
        rcseq=[]
        for h in range(0, len(rc)):
            if rc[h] == 'A':
                rcseq.append('T')
            elif rc[h] == 'T':
                rcseq.append('A')
            elif rc[h] == 'C':
                rcseq.append('G')
            elif rc[h] == 'G':
                rcseq.append('C')
        rcprim = ''.join(rcseq)
        print("......Coding Sequence...", frag)
        print("...Reverse Complement...", rcprim)
        print("......Primer Location...", j, '-', j+len(frag), 'bases')
        print("..................GC%...", (GC)[0])
        print("...................Tm...", 4*(len(GCcount))+2*(len(frag)-len(GCcount)),'C \n')