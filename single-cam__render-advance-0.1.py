# Render & Advance

import bpy

def save_render_and_advance(scene):

    # Save the Blender file
    bpy.ops.wm.save_mainfile()

    # !!! Set the rendering parameters- change location here !!!
    bpy.context.scene.render.filepath = "path/to/render/output/imagename" + f"{bpy.context.scene.frame_current}"

    # Render the current frame using the active camera
    bpy.ops.render.render(write_still=True)

    # Advance to the next frame
    bpy.context.scene.frame_set(bpy.context.scene.frame_current + 1)
    
# Add an event handler for the save operation
bpy.app.handlers.save_post.append(save_render_and_advance)