import pygame
import ObjectKu
class vertex:
    def __init__(self,nama,x,y,height,width, img) -> None:
        self.nama = nama
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.hitbox = (self.x+30, self.y+73,30,40)
        self.popUpImg = img
        self.hartaKarun = False # cek apakah ada harta karun
        self.visited = False # cek visited
    
    def draw(self,win):
        pygame.draw.rect(win,(255,0,0),self.hitbox,3)
    
    def collition(self, object: ObjectKu.object): # note ganti collision : titik tengah anjing  dengan tengah kotak 
        # garis kanan object dalan hitbox vertex
        if object.arahKanan:
            if object.x + object.width >= self.hitbox[0] + (self.hitbox[2]/2) and object.x + object.width <= self.hitbox[0]+ self.hitbox[2]:
                if object.y + object.height >= self.hitbox[1] + (self.hitbox[3]/2)and object.y + object.height <= self.hitbox[1] + self.hitbox[3]:
                    return True
                elif object.y >= self.hitbox[1] + (self.hitbox[3]/2) and object.y <= self.hitbox[1] + self.hitbox[3]:
                    return True
            
        # kiri beda kotak 
        elif not(object.arahKanan):
            if object.x >= self.hitbox[0]  and object.x <= self.hitbox[0] + (self.hitbox[2]/2):
                if object.y + object.height >= self.hitbox[1] + (self.hitbox[3]/2) and object.y + object.height <= self.hitbox[1] + self.hitbox[3]:
                    return True
                elif object.y >= self.hitbox[1] + (self.hitbox[3]/2)and object.y <= self.hitbox[1] + self.hitbox[3]:
                    return True
    
    def collition_titik(self, mouse_coor : list):
        if mouse_coor[0] >= self.hitbox[0] and mouse_coor[0] <= self.hitbox[0] + self.hitbox[2]:
            if mouse_coor[1] >= self.hitbox[1] and mouse_coor[1] <= self.hitbox[1] + self.hitbox[3]:
                return True
        return False

class Graph:
    def __init__(self) -> None:
            self.vertices = {}
            self.listVertex = {}
            self.count = 0

    def add_vertex(self, vertex: vertex) -> None:
        self.vertices[vertex] = []
        self.listVertex[vertex.nama] = vertex
        self.count += 1

    def add_edge(self, v1, v2) -> None:
        self.vertices[v1].append(v2)
        self.vertices[v2].append(v1)

    def print_adjacency_list(self,win) -> None:
        for vertex in self.vertices.items():
            vertex.draw(win)

    def printVerticels(self):
        for v in self.vertices.keys():
            print(v.nama , end=' :  ')
            for v2 in self.vertices[v]:
                print(v2.nama , end='   ')
            print()
        print()

    def dfs_path(self, startVName : str): # btw startV masih namanya
        # cek apakah ada di dalam key verticels
        visited = []
        path = []

        # tandai startV sek
        visited.append(self.listVertex[startVName])

        # masukin ke path juga
        path.append(self.listVertex[startVName])

        # rekursifnya
        for v2 in self.vertices[self.listVertex[startVName]]: # masih class verticles
            # jika belum di visited maka rekursi
            if not(v2 in visited):
                self.dfs_path_rec(self.listVertex[startVName], v2, path, visited)
        
        return path
    

    def dfs_path_rec(self, vPrev, vNow, path: list,  visited: list):
        # tandai vNow
        visited.append(vNow)

        # masukan ke dalam path juga
        path.append(vNow)

        # cek semua edge di vNow
        for v2 in self.vertices[vNow]: # masih class verticles
            # jika belum di visited maka rekursi
            if not(v2 in visited):
                self.dfs_path_rec(vNow,v2, path,visited)
        
        # backtrack ke v sebelumnya (lebih tepatnya kembali ke rekursi sebelumnya) maka masukin ke path dan jika semua belum divisit maka masukin ke path 
        if vPrev is not None and not(len(visited) == self.count) : 
            path.append(vPrev)
    
    def get_Arr(self): # radius prawiro ga masuk
        arr = []
        for i in self.listVertex.keys():
            # masukin ke dalam arr
            if not(i == 'Kolam Hijau'):
                arr.append(i)
        
        return arr
    
    def reset_visited(self):
        for i, j in self.listVertex.items():
            j.visited = False