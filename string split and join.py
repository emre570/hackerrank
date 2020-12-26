#burası siteye göre kodu uygulamaya çalıştığım yer

def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
  
#alt taraf da benim yazdığım ve çalışan kod
a = input()
a = a.split(" ")
a = "-".join(a)
print(a)
