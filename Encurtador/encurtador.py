import pyshorteners

link = input("Digite sua URL: ")

linkV = pyshorteners.Shortener()

link_curto = linkV.tinyurl.short(link)


print(f"O seu link encurtado é: {link_curto}")