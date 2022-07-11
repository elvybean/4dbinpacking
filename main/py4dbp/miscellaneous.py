from py4dbp.packer import Packer

def select(packer: Packer):
    for b in packer.bins:
        if len(b.unfitted_items) == 0:
            print("Appropriate bin found\n")

            print(":::::::::::", b.string())

            print("FITTED ITEMS:")
            for item in b.items:
                print("====> ", item.string())

            return