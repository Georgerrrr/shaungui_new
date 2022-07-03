import glfw

glfw.init() 

windows = []

def start():
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CLIENT_API, glfw.OPENGL_API)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, True)

    while windows:
        print(len(windows))
        for window in windows:
            window.render()

        glfw.poll_events()
    glfw.terminate()

def add_window(window):
    if len(windows) >= 1:
        print("Warning: Only One Window Can Be Opened At One Point In Time")
        return
    windows.append(window)

def remove_window(window):
    windows.remove(window)
