import tkinter as tk
import math

class MiniMinecraft:
    def __init__(self, root):
        self.root = root
        self.root.title("Python 3D Block World")
        
        self.width = 800
        self.height = 600
        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg="skyblue")
        self.canvas.pack()

        # Camera state
        self.cam_x = 0.0
        self.cam_y = 2.0
        self.cam_z = -5.0
        self.yaw = 0.0
        self.pitch = 0.0

        # World state: set of 3D integer coordinates (x, y, z)
        self.blocks = set()
        for x in range(-2, 3):
            for z in range(1, 6):
                self.blocks.add((x, 0, z))

        # Mouse tracking
        self.last_mouse_x = None
        self.last_mouse_y = None

        # Bind controls
        self.canvas.bind("<B1-Motion>", self.rotate_camera)
        self.canvas.bind("<ButtonRelease-1>", self.reset_mouse)
        self.canvas.bind("<Button-1>", self.handle_click)
        self.canvas.bind("<Button-3>", self.handle_click)  # Right click
        self.root.bind("<KeyPress>", self.handle_keypress)

        self.draw_scene()

    def reset_mouse(self, event):
        self.last_mouse_x = None
        self.last_mouse_y = None

    def rotate_camera(self, event):
        if self.last_mouse_x is not None and self.last_mouse_y is not None:
            dx = event.x - self.last_mouse_x
            dy = event.y - self.last_mouse_y
            self.yaw += dx * 0.005
            self.pitch -= dy * 0.005
            self.pitch = max(-1.5, min(1.5, self.pitch))
        self.last_mouse_x = event.x
        self.last_mouse_y = event.y
        self.draw_scene()

    def project(self, x, y, z):
        """Project 3D world coordinates to 2D canvas coordinates."""
        # Translate relative to camera
        dx = x - self.cam_x
        dy = y - self.cam_y
        dz = z - self.cam_z

        # Rotate around Yaw (Y axis)
        cos_y, sin_y = math.cos(-self.yaw), math.sin(-self.yaw)
        x1 = dx * cos_y - dz * sin_y
        z1 = dx * sin_y + dz * cos_y

        # Rotate around Pitch (X axis)
        cos_p, sin_p = math.cos(-self.pitch), math.sin(-self.pitch)
        y2 = dy * cos_p - z1 * sin_p
        z2 = dy * sin_p + z1 * cos_p

        if z2 <= 0.1:  # Behind camera
            return None

        # Perspective projection
        fov = 400
        screen_x = self.width / 2 + (x1 * fov / z2)
        screen_y = self.height / 2 - (y2 * fov / z2)
        return screen_x, screen_y, z2

    def draw_scene(self):
        self.canvas.delete("all")
        
        # Draw crosshair
        cx, cy = self.width / 2, self.height / 2
        self.canvas.create_line(cx - 8, cy, cx + 8, cy, fill="white")
        self.canvas.create_line(cx, cy - 8, cx, cy + 8, fill="white")

        # Collect faces to draw
        polygons = []
        
        # Define 6 faces of a unit cube [x, y, z] to [x+1, y+1, z+1]
        cube_faces = [
            # Front, Back, Top, Bottom, Left, Right
            ([(0,0,1), (1,0,1), (1,1,1), (0,1,1)], "#32cd32"), # Front (Green)
            ([(0,0,0), (0,1,0), (1,1,0), (1,0,0)], "#228b22"), # Back
            ([(0,1,0), (0,1,1), (1,1,1), (1,1,0)], "#7ec850"), # Top
            ([(0,0,0), (1,0,0), (1,0,1), (0,0,1)], "#8b4513"), # Bottom
            ([(0,0,0), (0,0,1), (0,1,1), (0,1,0)], "#2e8b57"), # Left
            ([(1,0,0), (1,1,0), (1,1,1), (1,0,1)], "#2e8b57")  # Right
        ]

        for bx, by, bz in self.blocks:
            for vertices, color in cube_faces:
                pts = []
                avg_z = 0
                valid = True
                for vx, vy, vz in vertices:
                    proj = self.project(bx + vx, by + vy, bz + vz)
                    if proj is None:
                        valid = False
                        break
                    pts.extend([proj[0], proj[1]])
                    avg_z += proj[2]
                
                if valid:
                    avg_z /= 4
                    polygons.append((avg_z, pts, color, (bx, by, bz)))

        # Painter's Algorithm: Sort faces from back to front
        polygons.sort(key=lambda item: item[0], reverse=True)

        for _, pts, color, _ in polygons:
            self.canvas.create_polygon(pts, fill=color, outline="black")

    def handle_keypress(self, event):
        speed = 0.3
        forward_x = math.sin(self.yaw) * speed
        forward_z = math.cos(self.yaw) * speed
        right_x = math.cos(self.yaw) * speed
        right_z = -math.sin(self.yaw) * speed

        key = event.keysym.lower()
        if key == 'w':
            self.cam_x += forward_x
            self.cam_z += forward_z
        elif key == 's':
            self.cam_x -= forward_x
            self.cam_z -= forward_z
        elif key == 'a':
            self.cam_x -= right_x
            self.cam_z -= right_z
        elif key == 'd':
            self.cam_x += right_x
            self.cam_z += right_z
        elif key == 'space':
            self.cam_y += speed
        elif key == 'shift_l' or key == 'control_l':
            self.cam_y -= speed

        self.draw_scene()

    def handle_click(self, event):
        # Raycast along camera direction to find target block
        dx = math.sin(self.yaw) * math.cos(self.pitch)
        dy = math.sin(self.pitch)
        dz = math.cos(self.yaw) * math.cos(self.pitch)

        curr_x, curr_y, curr_z = self.cam_x, self.cam_y, self.cam_z
        last_grid = None

        for _ in range(50):
            curr_x += dx * 0.1
            curr_y += dy * 0.1
            curr_z += dz * 0.1
            grid = (math.floor(curr_x), math.floor(curr_y), math.floor(curr_z))

            if grid in self.blocks:
                if event.num == 1:  # Left Click: Break
                    self.blocks.remove(grid)
                elif event.num == 3 and last_grid:  # Right Click: Place
                    self.blocks.add(last_grid)
                self.draw_scene()
                break
            last_grid = grid

root = tk.Tk()
app = MiniMinecraft(root)
root.mainloop()