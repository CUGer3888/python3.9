from ultralytics import YOLO

if __name__ == "__main__":
    # 加载预训练模型
    model = YOLO("yolov8n.pt")

    # 开始训练
    model.train(
        data="dataset\\mars.yaml",
        epochs=1000,
        imgsz=640,
        device="0",
    )
# model: 这通常指的是一个已经定义好的神经网络模型对象，它包含了模型的结构和权重。在这个上下文中，它可能是 YOLO 模型的一个实例。
#
# data: 这个参数指定了包含训练、验证和测试数据的配置文件的路径。在 YOLO 框架中，mars.yaml 文件通常包含有关数据集的信息，比如类别数量、类别名称以及训练集、验证集和测试集的图像和标注文件的路径。
#
# epochs: 这个参数定义了模型将在整个数据集上迭代多少次。在这个例子中，epochs=1000 意味着模型将被训练 1000 个周期，即每个样本都会被看到 1000 次。
#
# imgsz: 这个参数设置了输入图像的尺寸。在这里，imgsz=640 意味着所有的图像在输入到模型之前都将被调整为 640x640 像素。
#
# device: 这个参数指定了训练将在哪个设备上运行。在这里，device="0" 通常意味着训练将在编号为 0 的 GPU 上进行。如果系统中有多个 GPU，可以通过改变这个数字来指定不同的 GPU。如果系统没有 GPU，可以将这个参数设置为 device="cpu" 来进行 CPU 上的训练。