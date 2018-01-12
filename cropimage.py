from PIL import Image

def crop(path, file):
	im = Image.open(path+'/origin/'+file)   
	img_size = im.size
	w = im.size[0]
	h = im.size[1]

	#print("xx:{}".format(img_size))

	region = im.crop((70/1080*w,220/1920*h, w-70/1080*w,1200/1920*h))    #裁剪的区域
	saved_name = 'crop_'+file
	region.save(path + "/crop/"+saved_name)

	return [saved_name, [w, h]]