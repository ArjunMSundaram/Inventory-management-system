record={116051:{'Name':'Lays','Type':'Chips','Flavor':'Creamy onion','price':'Rs.5','Expiry':'12/6/2021','In stock':1500},
        116052:{'Name':'Lays','Type':'Chips','Flavor':'Indian masala','price':'Rs.5','Expiry':'12/6/2021','In stock':1500},
        116053:{'Name':'Lays','Type':'Chips','Flavor':'Naughty tomato','price':'Rs.5','Expiry':'12/6/2021','In stock':1500},
        116054:{'Name':'Lays','Type':'Chips','Flavor':'Maxx','price':'Rs.20','Expiry':'15/9/2021','In stock':2000},
        115021:{'Name':'Cheetos','Type':'Chips','Flavor':'Cheese corn','price':'Rs.5','Expiry':'12/6/2021','In stock':1200},
        115023:{'Name':'Cheetos','Type':'Chips','Flavor':'Puff corn','price':'Rs.5','Expiry':'17/6/2022','In stock':1200},
        113031:{'Name':'Tropicana','Type':'Juice','Flavor':'Strawberry','price':'Rs.250','Expiry':'31/12/2021','In stock':1000},
        113032:{'Name':'Tropicana','Type':'Juice','Flavor':'Orange','price':'Rs.250','Expiry':'31/12/2021','In stock':1000},
        113034:{'Name':'Tropicana','Type':'Juice','Flavor':'Pomegrannate','price':'Rs.250','Expiry':'31/12/2021','In stock':1000},
        113036:{'Name':'Coca cola','Type':'Soft drink','Flavor':'Cola','price':'Rs.75','Expiry':'31/6/2022','In stock':1100},
        117056:{'Name':'Maaza','Type':'Juice','Flavor':'Mango','price':'Rs.50','Expiry':'17/11/2021','In stock':1100},
        113037:{'Name':'Red bull','Type':'Soft drink','Flavor':'Sugar free','price':'Rs.350','Expiry':'31/12/2022','In stock':1250},
        113038:{'Name':'Red bull','Type':'Soft drink','Flavor':'Watermelon','price':'Rs.350','Expiry':'31/12/2022','In stock':1250},
        123032:{'Name':'Gillete','Type':'Shaving cream','Flavor':'Cool menthol','price':'Rs.400','Expiry':'31/12/2022','In stock':500},
        123035:{'Name':'Gillete','Type':'Shaving cream','Flavor':'Fresh','price':'Rs.375','Expiry':'31/12/2022','In stock':500},
        123096:{'Name':'Gillete','Type':'Razor','Flavor':'Mach3','price':'Rs.500','Expiry':'-','In stock':300},
        123098:{'Name':'Gillete','Type':'Razor','Flavor':'Turbo','price':'Rs.450','Expiry':'-','In stock':270},
        134309:{'Name':'Cinthol','Type':'Soap','Flavor':'Original','price':'Rs.35','Expiry':'31/4/2022','In stock':250},
        134317:{'Name':'Cinthol','Type':'Soap','Flavor':'Fresh lime','price':'Rs.45','Expiry':'31/4/2022','In stock':200},
        134329:{'Name':'Dettol','Type':'Soap','Flavor':'Cool','price':'Rs.28','Expiry':'31/10/2022','In stock':300},
        134327:{'Name':'Dettol','Type':'Soap','Flavor':'Honey','price':'Rs.33','Expiry':'31/10/2022','In stock':300},
        174465:{'Name':'Colgate','Type':'Tooth paste','Flavor':'Strong teeth','price':'Rs.40','Expiry':'30/5/2022','In stock':800},
        174467:{'Name':'Colgate','Type':'Tooth paste','Flavor':'Active salt','price':'Rs.48','Expiry':'17/9/2022','In stock':650},
        174469:{'Name':'Colgate','Type':'Tooth paste','Flavor':'Vedshakthi','price':'Rs.55','Expiry':'30/5/2022','In stock':400},
        174461:{'Name':'Colgate','Type':'Tooth paste','Flavor':'Max fresh','price':'Rs.36','Expiry':'16/2/2022','In stock':350},
        174468:{'Name':'Pears','Type':'Soap','Flavor':'Glycerine','price':'Rs.49','Expiry':'18/4/2022','In stock':250},
        198655:{'Name':'Dairy milk','Type':'Chocolate','Flavor':'Fruit&nut','price':'Rs.80','Expiry':'31/12/2021','In stock':500},
        198656:{'Name':'Dairy milk','Type':'Chocolate','Flavor':'Bubbly','price':'Rs.150','Expiry':'31/10/2021','In stock':450},
        198657:{'Name':'Dairy milk','Type':'Chocolate','Flavor':'Mousse','price':'Rs.200','Expiry':'30/11/2021','In stock':400},
        198658:{'Name':'Dairy milk','Type':'Chocolate','Flavor':'Caramilk','price':'Rs.90','Expiry':'31/10/2021','In stock':200},
        198237:{'Name':'Boomer','Type':'Chewing gum','Flavor':'Strawberry','price':'Rs.1','Expiry':'28/3/2021','In stock':1000},
        198238:{'Name':'Boomer','Type':'Chewing gum','Flavor':'Banana','price':'Rs.1','Expiry':'28/3/2021','In stock':900},
        198239:{'Name':'Boomer','Type':'Chewing gum','Flavor':'Orange','price':'Rs.1','Expiry':'28/3/2021','In stock':800}}

keys=[]
for w in record.keys():
    keys.append(w)
n=int(input("Enter the number of items to be billed"))
i=1
while(i<=n):
    print("Enter the product id of item",i)
    ids=int(input())
    if ids  in keys:
        q=int(input("Enter the quantity"))
        for key in record:
            if(key==ids):
               record[ids]['In stock'] = record[ids]['In stock']-q
    else:
        print("Invalid key")
        continue
    i+=1
for hg in record.items():
    print(hg)
    
