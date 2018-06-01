# Reading Training data with around 1690 Row and 18 columns from csv

##################### Training Data ########################################################
trainingdata <- read.csv('Training Data.csv',stringsAsFactors = FALSE)
############################################################################################

# Reading Test Data with 200 Row and 6 column csv 
###################### Testing Data ########################################################
testdata <- read.csv('Test Data.csv',stringsAsFactors = FALSE)
############################################################################################

# Data Pre-processing
# Remove the columns not required as the part of creating a model

############################# Remove Columns ###############################################
trainingdata <- trainingdata[,c(-1,-2,-3,-4,-6,-12,-15,-16,-17)]
############################################################################################

# Remove IELTS Column
testdata <- testdata[,c(-5)]
############################################################################################

# Take mean of all the AWA values and subsitute the mean for n/a fields.
################################ For AWA ###################################################  
testdata$AWA = ifelse(is.na(testdata$AWA),
                      ave(testdata$AWA, FUN = function(x) mean(x, na.rm = T)),
                      testdata$AWA)
trainingdata$AWA = ifelse(is.na(trainingdata$AWA),
                          ave(trainingdata$AWA, FUN = function(x) mean(x, na.rm = T)),
                          trainingdata$AWA)
############################################################################################

################################ For TOEFL #################################################
trainingdata$TOEFL = ifelse(is.na(trainingdata$TOEFL),
                            ave(trainingdata$TOEFL, FUN = function(x) mean(x, na.rm = T)),
                            trainingdata$TOEFL)

testdata$TOEFL = ifelse(is.na(testdata$TOEFL),
                        ave(testdata$TOEFL, FUN = function(x) mean(x, na.rm = T)),
                        testdata$TOEFL)
############################################################################################


# Change the categorical data to numerical values.	
#################################### For Result ############################################
trainingdata$Result = factor(trainingdata$Result,
                             levels = c('Accept', 'Reject'),
                             labels = c(1, 0))

testdata$Result = factor(testdata$Result,
                         levels = c('Accept', 'Reject'),
                         labels = c(1, 0))
############################################################################################

#Convert percentage to numeric value	
trainingdata$Percentage <- as.numeric(trainingdata$Percentage);

#ignore the records which contains n/a percentage values 
trainingdata <- trainingdata[which(is.na(trainingdata$Percentage) == FALSE),]

#Considering only Cs major data and removing other skewed data.
trainingdata <- trainingdata[which(trainingdata$Major == 'CS'),c(-2,-7,-8)]
trainingdata <- trainingdata[,c(-3)]
trainingdata

#Convert percentage to numeric value
testdata$Percentage <- as.numeric(testdata$Percentage);

#ignore the records which contains n/a percentage values 
testdata <- testdata[which(is.na(testdata$Percentage) == FALSE),]
############################################################################################

############################ Feature Scaling ###############################################
trainingdata[-1] = scale(trainingdata[-1])
testdata[-1] = scale(testdata[-1])
############################################################################################

################################# Model Implementations ####################################

############################### RandomForest ###############################################

install.packages('randomForest')

# load the library
library(randomForest)

# create a random forest classifier or model 
classifier = randomForest(x = trainingdata[-1],
                          y = trainingdata$Result,
                          ntree = 70)
#                         ntree = 500)
# we can use more trees, say, ntree = 500 
# But be careful with overfiting -- too many trees may not be helpful

# predict the test data result based on model created.
y_pred = predict(classifier, newdata = testdata[-1])

# Making the Confusion Matrix
cm = table(testdata[, 1], y_pred)
cm
error_rate = (cm[1,2]+cm[2,1])/199
error_rate

# plot the data 
plot(classifier)
legend("topright",colnames(classifier$err.rate),col=1:3,cex=0.8,fill=1:3)

############################################################################################

############################### Naive Bayes ################################################

install.packages('e1071')

# load the library
library(e1071)

# create a naive bayes classifier or model 
classifier <- naiveBayes(Result ~ ., data  = trainingdata)
class(classifier)

print(classifier)

# predict the test data result based on model created.
y_pred <- predict(classifier, newdata = testdata[-1])
y_pred

# Making the Confusion Matrix
cm = table(testdata[, 1], y_pred)
cm
##############################################################################################

################################ Decision Tree ###############################################

#install.packages('tree')

# load the library
# library(rpart)
# 
# # create a decision tree classifier or model 
# classifier = rpart(formula = Result ~ .,data = trainingdata)
# 
# # predict the test data result based on model created.
# y_pred = predict(tree.model, newdata = testdata[-1], type='class')
# y_pred
# 
# # Making the Confusion Matrix
# cm = table(testdata[, 1], y_pred)
# cm

# plot the data 
# plot(classifier)
# text(classifier, cex=.75)

install.packages('tree')
# load the library
library(tree)
# create a decision tree classifier or model 
classifier <- tree(Result ~., data=trainingdata)
# plot the Model 
plot(classifier)
text(classifier, cex=.75)
# predict the test data result based on model created.
y_pred = predict(classifier, newdata = testdata[-1], type='class')
y_pred
# Making the Confusion Matrix
cm = table(testdata[, 1], y_pred)
cm

###############################################################################################

############################### SVM Model - Linear ############################################

#install.packages('e1071')

# load the library
library(e1071)

# create a svm classifier or model 
classifier = svm(formula = Result ~ .,data = trainingdata,type = 'C-classification',kernel = 'linear')

# predict the test data result based on model created.
y_pred = predict(classifier, newdata = testdata[-1])
y_pred

# Making the Confusion Matrix
cm = table(testdata[, 1], y_pred)
cm
################################################################################################

############################ SVM Model - Kernel ################################################

#install.packages('e1071')

# load the library
library(e1071)

# create a svm classifier or model 
classifier = svm(formula = Result ~ .,data = trainingdata,type = 'C-classification',kernel = 'radial')

# predict the test data result based on model created.
y_pred = predict(classifier, newdata = testdata[-1])
y_pred

# Making the Confusion Matrix
cm = table(testdata[, 1], y_pred)
cm
##################################################################################################