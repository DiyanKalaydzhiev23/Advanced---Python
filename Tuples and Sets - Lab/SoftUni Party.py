invitations = set()
came = set()
[invitations.add(input()) for _ in range(int(input()))]

info = input()

while info != "END":
    came.add(info)
    info = input()

not_coming = sorted(invitations.difference(came))
print(len(not_coming))
[print(el) for el in not_coming]
