def addNoiseByChannel(img_path):
    origin_img = cv2.imread(img_path)   # BGR
    # 分割通道
    (b, g, r) = cv2.split(origin_img)
    # 或者只需要取某个单独通道
    # b = cv2.split(origin_img)[0]
    # g = cv2.split(origin_img)[1]
    # g = cv2.split(origin_img)[2]

    # add gaussian noise in channel blue only 
    b_noise_img = skimage.util.random_noise(b, mode='gaussian', seed=None, clip=True)
    cv2.namedWindow('noise_img')
    cv2.imshow('b',b)
    cv2.imshow('b_noise_img',b_noise_img)
    # 在 skimage.util.random_noise中, 图像将会被转换为float64类型的
    # 因此在合并的时候，g和r通道的图像也应该转换为float64类型的，才能成功合并通道
    g = skimage.util.img_as_float(g)
    cv2.imshow('g',g)
    r = skimage.util.img_as_float(r)
    cv2.imshow('r',r)
    # print b_noise_img.dtype, g.dtype, r.dtype
    # 合并通道
    noise_img = cv2.merge([b_noise_img, g, r])
    cv2.imshow('noise_img',noise_img)