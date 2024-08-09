# 环境配置

==vs2022和cuda11.1冲突    cuda11.1只能用2017 2019==



cmake版本高    编译python会报错[Policy CMP0148 is not set: The FindPythonInterp and FindPythonLibs modules](https://blog.csdn.net/u010933982/article/details/134457135)

所以最好python和js勾都去掉



[windows安装tensorrt 装的8.6 -CSDN博客](https://blog.csdn.net/m0_37605642/article/details/127583310)



[【CUDA】cuda安装 （windows版）_windows安装cuda_何为xl的博客-CSDN博客](https://blog.csdn.net/weixin_43848614/article/details/117221384)



[windows下安装Visual Studio + CMake+OpenCV + OpenCV contrib+TensorRT](https://blog.csdn.net/qq_40716944/article/details/131297563) 

没看但是挺全







## [PCL 1.13.0 + VS2022 安装配置教程_pcl安装-CSDN博客](https://blog.csdn.net/m0_46231910/article/details/130394937?spm=1001.2101.3001.6650.7&utm_medium=distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~Rate-7-130394937-blog-130770476.235^v39^pc_relevant_3m_sort_dl_base1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~Rate-7-130394937-blog-130770476.235^v39^pc_relevant_3m_sort_dl_base1&utm_relevant_index=14)

VS2022+QT5+VTK9.2.1+PCL1.13.1

[VTK不完整需要重新编译](https://blog.csdn.net/mjmald/article/details/133828390)

![image-20231206143715546](.\img\image-20231206143715546.png)



## [OPENCV4.5.1安装](https://blog.csdn.net/w2492602718/article/details/134316125)

[cmake 编译opencv4.5.5 ](https://blog.csdn.net/qq_35275007/article/details/130909961)==写的最全最后用这个过了！==



4.5.1报错

```
#error:  -- unsupported Microsoft Visual Studio version! Only the versions between 2017 and 2019 (inclusive) are supported! The nvcc flag '-allow-unsupported-compiler' can be used to override this version check; however, using an unsupported host compiler may cause compilation failure or incorrect run time execution. Use at your own risk.	opencv_world	D:\NVIDIA GPU Computing Toolkit\CUDA\v11.1\include\crt\host_config.h	160		
```

[==cuda11.1只支持2017 2019==](https://blog.csdn.net/Kasper_2009/article/details/130384029)



下载缺包开vpn多试https://blog.csdn.net/weixin_46135347/article/details/114190250

![image-20231208081053069](.\img\image-20231208081053069.png)

[勾选cuda](https://blog.csdn.net/stq054188/article/details/132766965)

![image-20231208174026300](.\img\image-20231208174026300.png)

![image-20231209003130478](.\img\image-20231209003130478.png)



[hashmap_compare 不是在std](https://blog.csdn.net/xiaosier_D/article/details/132298267)

[VIsual Studio编译OpenCV opencv_contrib：无法打开python36_d.lib的问题](https://www.jianshu.com/p/9ecc4948246f)



# 深度学习部署

## 查看onnx网址

https://netron.app/



## libtorch



## [opencv+ onnx 推理](https://github.com/UNeedCryDear/yolov7-opencv-dnn-cpp)     √

他的代码直接能用还简单但是不通用深度学习的模型

==环境THU==

```
python path/to/export.py --weights yolov7.pt --img [640,640]
```

请注意，yolov7导出的时候不要加--grid这个参数(控制detect层),否则opencv读取没问题，推理报错.



![image-20231205155533372](.\img\image-20231205155533372.png)

```
parser.add_argument('--grid', action='store_true', help='export Detect() layer grid')
```

yolov7_cv.onnex 可以看到输出是没有gather一起的

## 自动驾驶之心的博客    ×

[手把手教程 | 如何用TensorRT部署YOLOv7_自动驾驶之心的博客-CSDN博客](https://blog.csdn.net/CV_Autobot/article/details/128246444)

[手把手教学！TensorRT部署实战：YOLOv5的ONNX模型部署](https://mp.weixin.qq.com/s?__biz=MzkwNjE2ODMyMQ==&mid=2247484676&idx=1&sn=b5f10a09ef5cbc5251da590d92726b24&chksm=c0edd46af79a5d7ccc730eb5fc844f07137589b57e88810b4eb9563df976f6144bb5db3908e7&token=916135679&lang=zh_CN#rd)

```c++
void Detector::CreatEngineFile(std::string model_path, const std::string  engine_file_path)
{
	//通过logger创建IBuilder
	MyLogger logger;
	nvinfer1::IBuilder* builder = nvinfer1::createInferBuilder(logger);
	//通过IBuilder创建network
	const uint32_t explicit_batch = 1U << static_cast<uint32_t>(nvinfer1::NetworkDefinitionCreationFlag::kEXPLICIT_BATCH);
	nvinfer1::INetworkDefinition* network = builder->createNetworkV2(explicit_batch);
	//创建ONNX解析器对象
	nvonnxparser::IParser* parser = nvonnxparser::createParser(*network, logger);
	parser->parseFromFile(model_path.c_str(),static_cast<int>(nvinfer1::ILogger::Severity::kERROR));
	// 如果有错误则输出错误信息
	for (int32_t i = 0; i < parser->getNbErrors(); ++i) {
		std::cout << parser->getError(i)->desc() << std::endl;
	}
	//通过IBuilder创建IBuilderConfig对象来告诉TensorRT该如何对模型进行优化。这个接口定义了很多属性，
	// 其中最重要的一个属性是工作空间的最大容量。在网络层实现过程中通常会需要一些临时的工作空间，这
	// 个属性会限制最大能申请的工作空间的容量，如果容量不够的话会导致该网络层不能成功实现而导致错误。
	// 另外，还可以通过这个对象设置模型的数据精度。TensorRT默认的数据精度为FP32，我们还可以设置FP16
	// 或者INT8，前提是该硬件平台支持这种数据精度。
	nvinfer1::IBuilderConfig* config = builder->createBuilderConfig();
	config->setMemoryPoolLimit(nvinfer1::MemoryPoolType::kWORKSPACE, 1U << 27);
	//启动优化引擎对模型进行优化了经过TensorRT优化后的序列化模型被保存到IHostMemory对象中，我们可以将其保存到磁盘中，
	//下次使用时直接加载这个经过优化的模型即可，这样就可以省去漫长的等待模型优化的过程。我一般习惯把序列化模型保存到一个后缀为.engine的文件中
	nvinfer1::IHostMemory* serialized_model =
		builder->buildSerializedNetwork(*network, *config);

	// 将模型序列化到engine文件中
	std::stringstream engine_file_stream;
	engine_file_stream.seekg(0, engine_file_stream.beg);
	engine_file_stream.write(static_cast<const char*>(serialized_model->data()),
		serialized_model->size());
	std::ofstream out_file(engine_file_path);
	assert(out_file.is_open());
	out_file << engine_file_stream.rdbuf();
	out_file.close();
	delete config;
	delete parser;
	delete network;
	delete builder;
	return;
}
```

```c++


void Detector::InitModel(std::string engine_file_path)
{
	//直接从磁盘中加载.engine文件
	MyLogger logger;
	std::stringstream engine_file_stream;
	engine_file_stream.seekg(0, engine_file_stream.beg);
	std::ifstream ifs(engine_file_path);
	if (!ifs.is_open()) {
		// 处理文件打开失败的情况
		std::cout << "open engine_file_path error!"<<  std::endl;
	}
	engine_file_stream << ifs.rdbuf();
	ifs.close();

	engine_file_stream.seekg(0, std::ios::end);
	const int model_size = engine_file_stream.tellg();
	std::cout << "model_size:" << model_size  << std::endl;
	engine_file_stream.seekg(0, std::ios::beg);
	void* model_mem = malloc(model_size);
	engine_file_stream.read(static_cast<char*>(model_mem), model_size);

	//通过IRuntime接口对模型进行反序列化
	nvinfer1::IRuntime* runtime = nvinfer1::createInferRuntime(logger);
	//engine对象中存放着经过TensorRT优化后的模型
	nvinfer1::ICudaEngine* engine = runtime->deserializeCudaEngine(model_mem, model_size);
	if (engine == nullptr) {
		printf("Deserialize cuda engine failed.\n");
		runtime->destroy();
		return;
	}
	delete runtime;
	free(model_mem);

	//要用模型进行推理则还需要通过createExecutionContext()函数去创建一个IExecutionContext对象来管理推理的过程
	this->context = engine->createExecutionContext();

	// 获取模型输入尺寸并分配GPU内存
	nvinfer1::Dims input_dim = engine->getBindingDimensions(0);
	this->input_size = 1;
	for (int j = 0; j < input_dim.nbDims; ++j) {
		this->input_size *= input_dim.d[j];
	}
	cudaMalloc(&this->buffers[0], this->input_size * sizeof(float));

	// 获取模型输出尺寸并分配GPU内存
	nvinfer1::Dims output_dim = engine->getBindingDimensions(1);
	this->output_size = 1;
	for (int j = 0; j < output_dim.nbDims; ++j) {
		this->output_size *= output_dim.d[j];
	}
	cudaMalloc(&this->buffers[1], this->output_size * sizeof(float));

	// 给模型输出数据分配相应的CPU内存
	float* output_buffer = new float[this->output_size]();
	return;
}
```

有坑，代码应该有问题

生成engine大小每次都不一样

加载engine一直报错

![image-20231204231746549](.\img\image-20231204231746549.png)

## [trtexec 生成 engine](https://mp.weixin.qq.com/s/Xbk03XGcon9eU87F_B1a4Q)

[说的也很好](https://zhuanlan.zhihu.com/p/580268047)

注意，生成onnx模型的过程***不必\***在做推理的设备上运行，即可以使用性能强的服务器生成onnx。

生成 engine 模型的过程***必须\***在做推理的设备上运行



==ONNX Runtime=可能可以c++推理onnx但是和tensorRT代码改动大，所以现在其他设备用opencv==

```
 trtexec --onnx=yolov7.onnx --saveEngine=yolov7_16.engine --fp16
```

```c++
int main(int argc, char* argv[])
{
    // 引擎文件路径
    const std::string engineFile = ".\\models\\yolov7_16.engine";

    // 创建 TensorRT Logger
    MyLogger logger;

    // 创建 TensorRT 运行时
    nvinfer1::IRuntime* runtime = nvinfer1::createInferRuntime(logger);

    // 读取引擎文件
    std::ifstream engineFileStream(engineFile, std::ios::binary);
    if (!engineFileStream) {
        std::cerr << "Error: Unable to open engine file: " << engineFile << std::endl;
        return 1;
    }
    engineFileStream.seekg(0, std::ios::end);
    const size_t engineSize = engineFileStream.tellg();
    engineFileStream.seekg(0, std::ios::beg);
    std::vector<char> engineData(engineSize);
    engineFileStream.read(engineData.data(), engineSize);
    engineFileStream.close();

    // 反序列化引擎
    nvinfer1::ICudaEngine* engine = runtime->deserializeCudaEngine(engineData.data(), engineSize);
    if (!engine) {
        std::cerr << "Error: Unable to deserialize CUDA engine." << std::endl;
        return 1;
    }
    nvinfer1::IExecutionContext* context = engine->createExecutionContext();
    if (!context) {
        std::cerr << "Error: Unable to create execution context." << std::endl;
        return 1;
    }



    void* buffers[2];
    // 获取模型输入尺寸并分配GPU内存
    nvinfer1::Dims input_dim = engine->getBindingDimensions(0);
    int input_size = 1;
    for (int j = 0; j < input_dim.nbDims; ++j) {
        input_size *= input_dim.d[j];
    }
    cudaMalloc(&buffers[0], input_size * sizeof(float));

    // 获取模型输出尺寸并分配GPU内存
    nvinfer1::Dims output_dim = engine->getBindingDimensions(1);
    int output_size = 1;
    for (int j = 0; j < output_dim.nbDims; ++j) {
        output_size *= output_dim.d[j];
    }
    cudaMalloc(&buffers[1], output_size * sizeof(float));

    // 给模型输出数据分配相应的CPU内存
    float* output_buffer = new float[output_size]();

    cudaStream_t stream;
    cudaStreamCreate(&stream);

    Detector* detector = new Detector();
    detector->LoadImg("C:\\Users\\33567\\Pictures\\联想截图\\1.png");

    // 拷贝输入数据
    cudaMemcpyAsync(buffers[0], detector->input_blob, input_size * sizeof(float),
        cudaMemcpyHostToDevice, stream);
    // 执行推理
    context->enqueueV2(buffers, stream, nullptr);
    // 拷贝输出数据
    cudaMemcpyAsync(output_buffer, buffers[1], output_size * sizeof(float),
        cudaMemcpyDeviceToHost, stream);

    cudaStreamSynchronize(stream);
    // 等待 CUDA 流上的所有操作完成
    cudaStreamSynchronize(stream);
    std::cout << "Output output_size:  " << output_size << std::endl;
    // 打印输出结果
    std::cout << "Output Result: ";
    for (int i = 0; i < output_size; ++i) {
        std::cout << i << " " << output_buffer[i] << std:: endl;
    }
    std::cout << std::endl;
    return 0;
}

```



### with  --end2end    ×

```
python export.py --weights ./yolov7.pt --grid --end2end --simplify --topk-all 100 --iou-thres 0.65 --conf-thres 0.35 --img-size 640 640
```

![image-20231205000721679](.\img\image-20231205000721679.png)

[解决error code 1](https://blog.csdn.net/a2824256/article/details/121262135)后还是nvinfer1::Dims output_dim = engine->getBindingDimensions(1);获得等于0输出没有值

![image-20231205105928144](.\img\image-20231205105928144.png)

推理的输入形状应该不对

### without  --end2end  √

```
 python export.py --weights ./yolov7.pt --grid --simplify --img-size 640 640 
```

1. 加--include-nms 调用engine会卡死
2.  获得的数据shape

![image-20231205155244882](.\img\image-20231205155244882.png)





![image-20231205153921017](.\img\image-20231205153921017.png)

![image-20231205153937753](.\img\image-20231205153937753.png)

![image-20231205155132127](.\img\image-20231205155132127.png)

==25200*85 = 2142000==

2. 输出是没有处理的 84个一循环     需要去NMS

![image-20231204235354019](.\img\image-20231204235354019.png)

3. --grid应该就会对xywh防缩偏移处理

   yolov7.onnx 和 yolov7_16.engine  是 坐标处理过的xywh就是图像的中心点x,y,w,h

![image-20231205161152260](.\img\image-20231205161152260.png)



![image-20231205161405730](.\img\image-20231205161405730.png)

## libtorch

![9c4ec4c82859bf446b415e24b8d5fdf4](/media/wangkai/新加卷/codenotes/项目/THU_c++/img/9c4ec4c82859bf446b415e24b8d5fdf4.png)



# 开发

## [PCL+Qt+VS之点云可视化软件开发  ](https://www.bilibili.com/video/BV1iK4y1Y7nC/?spm_id_from=333.880.my_history.page.click&vd_source=eef102f4fb053709a57c96d0c876628a)

==用的VTK9.2.1+PCL1.13.1版本比较新  一些函数名字变了==

```
SetRenderWindow->setRenderWindow

GetInteractor ->GetInteractor

/添加坐标轴
 this->viewer->addCoordinateSystem(1,0)         ->   this->viewer->addCoordinateSystem(1)
```





[Qt中添加VTK窗口并显示点云 版本差不多](https://www.cnblogs.com/houjinghao/p/17686805.html)

![image-20231206144057305](.\img\image-20231206144057305.png)

## [vs link输入  批生成lib  导入](https://blog.csdn.net/weixin_49347928/article/details/134312931)

# 语法

![image-20231204165534883](.\img\image-20231204165534883.png)

```c++
class MyLogger : public nvinfer1::ILogger {
public:
	explicit MyLogger(nvinfer1::ILogger::Severity severity =
		nvinfer1::ILogger::Severity::kWARNING)
		: severity_(severity) {}

	void log(nvinfer1::ILogger::Severity severity,
		const char* msg) noexcept override {
		if (severity <= severity_) {
			std::cerr << msg << std::endl;
		}
	}
	nvinfer1::ILogger::Severity severity_;
};

```

### explicit

必须显式构造

### noexcept

- `noexcept` 是一个指定函数异常规范（exception specification）的关键字。

- 在函数声明或定义中，noexcept 后面可以跟随一个表达式，或者直接使用 noexcept，表示函数不会抛出异常。例如：

  ```c++
  cppCopy codevoid myFunction() noexcept;
  void myFunction2() noexcept(true);  // 等效于上面的声明
  ```

- 如果函数在 `noexcept` 规定的情况下抛出了异常，`std::terminate` 会被调用，程序终止。

### override

- `override` 是用于指定派生类中的成员函数覆盖基类中的虚函数的关键字。
- 在派生类的函数声明或定义中，使用 `override` 表示该函数是一个覆盖基类虚函数的函数。

# [项目打包](https://www.bilibili.com/video/BV1vP4y1g7w1/?spm_id_from=333.934.top_right_bar_window_history.content.click&vd_source=eef102f4fb053709a57c96d0c876628a)



## [找到exe文件所依赖的dll文件工具](https://blog.csdn.net/xz1203/article/details/117665301)



## [Qt打包遇到找不到Qt platform plugin "windows"问题](https://blog.csdn.net/xzpblog/article/details/79126250)

不是整个platforms文件夹

不是winMM.dll

是整个plugin文件夹复制过去就好了

==cmake时候找了cudnn位置，所以vs编译了，所以lib移植到其他机器可能还真不行==

==cmake会编译还会下载==
