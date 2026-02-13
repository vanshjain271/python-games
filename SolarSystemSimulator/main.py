from vpython import *
import time, math, random, os
import planets as P

scene.title="Solar System 3D — Ultimate Edition"
scene.width=1280
scene.height=800
scene.background=color.black
scene.forward=vector(-1.4,-0.45,-2.4)
scene.userspin=True
scene.userzoom=True
scene.range=70

TIME_SPEED=7.0
ROT_SPEED=0.003
DIST_SCALE=7.4
TRAIL_LEN=220
ORBIT_STEPS=260
LABELS_ON=True
ORBITS_ON=True
TRAILS_ON=True
PAUSED=False
cinematic=False
focus=None
focus_iss=False

local_light(pos=vector(0,0,0), color=vector(1.0,0.97,0.85))
distant_light(direction=vector(1,-0.2,-0.4), color=vector(0.35,0.35,0.35))

def rgb255(r,g,b): return vector(r/255, g/255, b/255)

PALETTE={"Mercury":rgb255(170,170,170),"Venus":rgb255(210,90,70),"Earth":rgb255(60,130,230),"Moon":rgb255(200,200,200),"Mars":rgb255(210,80,60),"Jupiter":rgb255(205,160,105),"Saturn":rgb255(210,190,140),"Uranus":rgb255(170,230,230),"Neptune":rgb255(90,140,255),"Pluto":rgb255(200,190,150)}

def orbit_pts(a):
    pts=[]
    for i in range(ORBIT_STEPS):
        ang=2*math.pi*i/ORBIT_STEPS
        x=a*math.cos(ang)*DIST_SCALE
        y=a*math.sin(ang)*DIST_SCALE
        z=0.25*a*math.sin(ang*0.6)
        pts.append(vector(x,y,z))
    return pts

for _ in range(700):
    sphere(pos=vector(random.uniform(-420,420),random.uniform(-420,420),random.uniform(-420,420)), radius=0.9, color=color.white, emissive=True)

class BodyState:
    def __init__(self, body):
        self.body=body
        self.angle=random.random()*2*math.pi
        self.pos=vector(0,0,0)
        self.sphere=None
        self.label=None
        self.trail=None
        self.orbit=None
        self.children=[]

states={b.name:BodyState(b) for b in P.BODIES}
for b in P.BODIES:
    if b.parent: states[b.parent].children.append(b.name)

sun=states["Sun"]
sun.sphere=sphere(pos=vector(0,0,0), radius=2.6, color=color.yellow, emissive=True)

flares=[]
flare_timer=0
def create_flare():
    ang=random.random()*2*math.pi
    r=sun.sphere.radius
    start=vector(r*math.cos(ang), r*math.sin(ang), random.uniform(-0.3,0.3))
    obj=sphere(pos=start, radius=0.20, color=rgb255(255,90,10), emissive=True, opacity=0.9)
    flares.append({"obj":obj,"dir":norm(start)*random.uniform(0.12,0.22),"life":random.uniform(1.5,2.2)})
def update_flares(dt):
    global flares
    for f in flares:
        f["obj"].pos+=f["dir"]
        f["obj"].opacity*=0.93
        f["obj"].radius*=1.02
        f["life"]-=dt
    flares=[f for f in flares if f["life"]>0]

sizes={"Mercury":0.18,"Venus":0.30,"Earth":0.33,"Mars":0.22,"Jupiter":1.7,"Saturn":1.5,"Uranus":1.1,"Neptune":1.05,"Pluto":0.16}

for b in P.BODIES:
    if b.name=="Sun": continue
    st=states[b.name]
    col=PALETTE[b.name]
    r_vis=sizes.get(b.name,0.12)
    tex=None
    if b.name=="Earth": tex=textures.earth
    if b.name=="Jupiter": tex=textures.wood
    st.sphere=sphere(pos=vector(0,0,0), radius=r_vis, color=col, texture=tex, emissive=True)
    st.label=label(text=b.name, pos=vector(0,0,0), height=14, box=False, color=color.white, opacity=0.8, visible=LABELS_ON)
    st.trail=curve(color=col, radius=0.04, retain=TRAIL_LEN, visible=TRAILS_ON)
    st.orbit=curve(pos=orbit_pts(b.au), radius=0.05, color=color.gray(0.45), visible=ORBITS_ON)

earth=states["Earth"]
earth_dark=sphere(pos=earth.pos, radius=earth.sphere.radius*1.03, texture="https://i.ibb.co/QYf4V9q/earth-night-lights.jpg", opacity=0.35, emissive=True)
def update_earth_night():
    E=earth.pos
    L=norm(E-vector(0,0,0))
    earth_dark.pos=E
    earth_dark.axis=L

jup=states["Jupiter"]; jup.moons=[]
for dist,period in [(0.55,1.77),(0.82,3.55),(1.25,7.15),(1.90,16.69)]:
    m=sphere(radius=0.10, color=color.white, emissive=True)
    jup.moons.append({"obj":m,"a":dist,"w":2*math.pi/period,"ang":random.random()*2*math.pi})

sat=states["Saturn"]
tilt_sat=math.radians(26)
axis_sat=vector(0,math.cos(tilt_sat),math.sin(tilt_sat))
sat.r1=ring(pos=sat.pos, axis=axis_sat, radius=sat.sphere.radius*4.2, thickness=sat.sphere.radius*0.09, color=rgb255(220,210,180), opacity=0.6)
sat.r2=ring(pos=sat.pos, axis=axis_sat, radius=sat.sphere.radius*5.0, thickness=sat.sphere.radius*0.07, color=rgb255(250,240,210), opacity=0.35)

ura=states["Uranus"]
tilt_ura=math.radians(98)
axis_ura=vector(0,math.cos(tilt_ura),math.sin(tilt_ura))
ura.ring=ring(pos=ura.pos, axis=axis_ura, radius=ura.sphere.radius*2.6, thickness=ura.sphere.radius*0.09, color=rgb255(210,210,210), opacity=0.45)

asteroids=[]
for _ in range(900):
    a=random.uniform(2.2,3.6)*DIST_SCALE
    ang=random.uniform(0,2*math.pi)
    z=random.uniform(-0.12,0.12)
    rock=sphere(pos=vector(a*math.cos(ang),a*math.sin(ang),z), radius=random.uniform(0.015,0.03), color=rgb255(165,155,150), shininess=0)
    asteroids.append({"obj":rock,"a":a,"ang":ang,"w":random.uniform(0.00005,0.00012)})

comet=sphere(radius=0.20, color=color.cyan, emissive=True, make_trail=True, trail_color=color.cyan, trail_radius=0.04)
comet_ang=0

iss_alt=0.42
iss=box(size=vector(0.12,0.05,0.05), color=color.white, emissive=True)
panel1=box(size=vector(0.25,0.03,0.01), color=color.blue, emissive=True)
panel2=box(size=vector(0.25,0.03,0.01), color=color.blue, emissive=True)
ISS_ANG=random.random()*2*math.pi
ISS_W=2*math.pi/1.5
def update_iss(dt):
    global ISS_ANG
    ISS_ANG+=ISS_W*dt*TIME_SPEED
    x=(earth.body.au+iss_alt)*math.cos(ISS_ANG)*DIST_SCALE
    y=(earth.body.au+iss_alt)*math.sin(ISS_ANG)*DIST_SCALE
    p=vector(x,y,0)
    iss.pos=p
    iss.axis=vector(-math.sin(ISS_ANG),math.cos(ISS_ANG),0)
    panel1.pos=p+vector(0.15,0,0)
    panel2.pos=p-vector(0.15,0,0)

try:
    scene.append_to_caption("<audio id='bgm' src='space.mp3' autoplay loop></audio>")
except:
    pass

auto_time0=time.time()

def reset_view():
    global focus, cinematic, focus_iss, auto_time0
    scene.center=vector(0,0,0)
    scene.forward=vector(-1.4,-0.45,-2.4)
    focus=None
    cinematic=False
    focus_iss=False
    auto_time0=time.time()

def pick_focus(evt):
    global focus, cinematic, focus_iss
    if evt.pick in [iss,panel1,panel2]:
        focus_iss=True; cinematic=False; focus=None
    else:
        for name,st in states.items():
            if st.sphere is evt.pick:
                focus=name; cinematic=False; focus_iss=False
scene.bind("click", pick_focus)

def on_key(evt):
    global TIME_SPEED, PAUSED, LABELS_ON, ORBITS_ON, TRAILS_ON, cinematic, focus, focus_iss
    k=evt.key
    if k==' ': PAUSED=not PAUSED
    elif k in ['=','+']: TIME_SPEED=min(50,TIME_SPEED*1.4)
    elif k=='-': TIME_SPEED=max(0.4,TIME_SPEED/1.4)
    elif k.lower()=='l': LABELS_ON=not LABELS_ON; [setattr(st.label,"visible",LABELS_ON) for st in states.values()]
    elif k.lower()=='o': ORBITS_ON=not ORBITS_ON; [setattr(st.orbit,"visible",ORBITS_ON) for st in states.values()]
    elif k.lower()=='t': TRAILS_ON=not TRAILS_ON; [st.trail.clear() for st in states.values() if st.trail]
    elif k.lower()=='r': reset_view()
    elif k.lower()=='c': cinematic=True; focus=None; focus_iss=False
    elif k.lower()=='i': focus_iss=True; cinematic=False; focus=None
    elif k.isdigit():
        order=["Sun","Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune","Pluto"]
        i=int(k)
        if i<len(order): focus=order[i]; cinematic=False; focus_iss=False
scene.bind("keydown", on_key)

if not os.path.exists("frames"):
    os.mkdir("frames")
frame_id=0
record_video=False

def update_body(name, parent_pos, dt):
    st=states[name]; b=st.body
    if name=="Sun":
        st.pos=vector(0,0,0)
    else:
        w=(2*math.pi/b.period_days)*0.4
        st.angle+=w*(dt*TIME_SPEED)
        x=b.au*math.cos(st.angle)*DIST_SCALE
        y=b.au*math.sin(st.angle)*DIST_SCALE
        z=0.25*b.au*math.sin(st.angle*0.6)
        st.pos=parent_pos+vector(x,y,z)
    st.sphere.pos=st.pos
    if st.label: st.label.pos=st.pos+vector(0,st.sphere.radius*1.5,0)
    if st.trail and TRAILS_ON: st.trail.append(st.pos)
    if name=="Saturn":
        sat.r1.pos=st.pos; sat.r2.pos=st.pos; sat.r1.axis=axis_sat; sat.r2.axis=axis_sat
    if name=="Uranus":
        ura.ring.pos=st.pos; ura.ring.axis=axis_ura
    for child in st.children:
        update_body(child, st.pos, dt)

prev=time.time()

while True:
    rate(60)
    now=time.time(); dt=now-prev; prev=now
    if not PAUSED:
        update_body("Sun", vector(0,0,0), dt)
        update_earth_night()
        update_iss(dt)
        comet_ang+=dt*TIME_SPEED*0.03
        comet.pos=vector(16*math.cos(comet_ang),6.5*math.sin(comet_ang),0)
        for a in asteroids:
            a["ang"]+=a["w"]*dt*TIME_SPEED
            a["obj"].pos=vector(a["a"]*math.cos(a["ang"]), a["a"]*math.sin(a["ang"]), a["obj"].pos.z)
        jp=states["Jupiter"].pos
        for m in jup.moons:
            m["ang"]+=m["w"]*(dt*TIME_SPEED)
            mx=m["a"]*math.cos(m["ang"]); my=m["a"]*math.sin(m["ang"])
            m["obj"].pos=jp+vector(mx,my,0)
        flare_timer+=dt
        if flare_timer>random.uniform(2,4):
            flare_timer=0; create_flare()
        update_flares(dt)
    elapsed=now-auto_time0
    if focus_iss:
        scene.center=scene.center*0.85+iss.pos*0.15
    elif elapsed<14:
        scene.center=vector(0,0,0)
        scene.camera.pos=vector(34*math.cos(elapsed*0.12),6,34*math.sin(elapsed*0.12))
    elif cinematic:
        t=now
        scene.center=vector(0,0,0)
        scene.camera.pos=vector(34*math.cos(t*0.15),6,34*math.sin(t*0.15))
    elif focus in states:
        target=states[focus].pos
        scene.center=scene.center*0.92+target*0.08
    if record_video:
        img=f"frames/frame_{frame_id:04d}.png"
        scene.capture(img)
        frame_id+=1
    scene.caption=(f"Speed:{TIME_SPEED:.2f}x  Focus:{focus or ('ISS' if focus_iss else 'None')}  "
                   f"Orbits:{'On' if ORBITS_ON else 'Off'}  Labels:{'On' if LABELS_ON else 'Off'}  Trails:{'On' if TRAILS_ON else 'Off'}\n"
                   "SPACE Pause  +/- Speed  L Labels  O Orbits  T Trails  R Reset  C Cinematic  I Focus ISS  0-9 Focus Planet")
