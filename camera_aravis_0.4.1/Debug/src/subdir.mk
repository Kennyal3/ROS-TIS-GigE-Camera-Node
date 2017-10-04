################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CPP_SRCS += \
../src/camera_node.cpp 

OBJS += \
./src/camera_node.o 

CPP_DEPS += \
./src/camera_node.d 


# Each subdirectory must supply rules for building sources it contributes
src/%.o: ../src/%.cpp
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C++ Compiler'
	g++ -I/opt/ros/kinetic/include -I/opt/ros/kinetic/include/xmlrpcpp -I"/home/auto3/catkin_ws/src/camera_aravis_0.4.1/include/driver_base" -I/usr/lib/x86_64-linux-gnu/glib-2.0/include -I/home/auto3/aravis-0.4.1/src -I/usr/include/glib-2.0 -I"/home/auto3/catkin_ws/src/camera_aravis_0.4.1/cfg/cpp/camera_aravis" -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


