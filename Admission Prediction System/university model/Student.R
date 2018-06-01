# Read training data from csv for all the university

##################### Training Data ########################################################
ASU <- read.csv('ASU.csv',stringsAsFactors = FALSE)
clemson <- read.csv('clemson.csv',stringsAsFactors = FALSE)
IITchicago <- read.csv('IIT-chicago.csv',stringsAsFactors = FALSE)
MTU <- read.csv('MTU.csv',stringsAsFactors = FALSE)
NE_Boston <- read.csv('NE_Boston.csv',stringsAsFactors = FALSE)
RIT <- read.csv('RIT.csv',stringsAsFactors = FALSE)
U_southern_cal <- read.csv('U_southern_cal.csv',stringsAsFactors = FALSE)
UNC <- read.csv('UNC.csv',stringsAsFactors = FALSE)
UTA <- read.csv('UTA.csv',stringsAsFactors = FALSE)
UTD <- read.csv('UTD.csv',stringsAsFactors = FALSE)
############################################################################################

# Read testing data from csv 
###################### Testing Data ########################################################
testdata <- read.csv('Test Student Data.csv',stringsAsFactors = FALSE)
############################################################################################

# Data Pre-processing
# Remove the columns not required as the part of creating a model
############################# Remove Columns ###############################################
ASU <- ASU[,c(-1,-2,-3,-4,-6,-12,-15,-16,-17)]
clemson <- clemson[,c(-1,-2,-3,-4,-6,-12,-15,-16,-17)]
IITchicago <- IITchicago[,c(-1,-2,-3,-4,-6,-12,-15,-16,-17)]
MTU <- MTU[,c(-1,-2,-3,-4,-6,-12,-15,-16,-17)]
NE_Boston <- NE_Boston[,c(-1,-2,-3,-4,-6,-12,-15,-16,-17)]
RIT <- RIT[,c(-1,-2,-3,-4,-6,-12,-15,-16,-17)]
U_southern_cal <- U_southern_cal[,c(-1,-2,-3,-4,-6,-12,-15,-16,-17)]
UNC <- UNC[,c(-1,-2,-3,-4,-6,-12,-15,-16,-17)]
UTA <- UTA[,c(-1,-2,-3,-4,-6,-12,-15,-16,-17)]
UTD <- UTD[,c(-1,-2,-3,-4,-6,-12,-15,-16,-17)]
#############################################################################################

# Removing IELTS
testdata <- testdata[,c(-4)]

# Take mean of all the AWA values and subsitute the mean for n/a fields.
################################ For AWA ###################################################  
ASU$AWA = ifelse(is.na(ASU$AWA),
                 ave(ASU$AWA, FUN = function(x) mean(x, na.rm = T)),
                 ASU$AWA)
clemson$AWA = ifelse(is.na(clemson$AWA),
                     ave(clemson$AWA, FUN = function(x) mean(x, na.rm = T)),
                     clemson$AWA)
IITchicago$AWA = ifelse(is.na(IITchicago$AWA),
                        ave(IITchicago$AWA, FUN = function(x) mean(x, na.rm = T)),
                        IITchicago$AWA)
MTU$AWA = ifelse(is.na(MTU$AWA),
                 ave(MTU$AWA, FUN = function(x) mean(x, na.rm = T)),
                 MTU$AWA)
NE_Boston$AWA = ifelse(is.na(NE_Boston$AWA),
                       ave(NE_Boston$AWA, FUN = function(x) mean(x, na.rm = T)),
                       NE_Boston$AWA)
RIT$AWA = ifelse(is.na(RIT$AWA),
                 ave(RIT$AWA, FUN = function(x) mean(x, na.rm = T)),
                 RIT$AWA)
U_southern_cal$AWA = ifelse(is.na(U_southern_cal$AWA),
                            ave(U_southern_cal$AWA, FUN = function(x) mean(x, na.rm = T)),
                            U_southern_cal$AWA)
UNC$AWA = ifelse(is.na(UNC$AWA),
                 ave(UNC$AWA, FUN = function(x) mean(x, na.rm = T)),
                 UNC$AWA)
UTA$AWA = ifelse(is.na(UTA$AWA),
                 ave(UTA$AWA, FUN = function(x) mean(x, na.rm = T)),
                 UTA$AWA)

UTD$AWA = ifelse(is.na(UTD$AWA),
                 ave(UTD$AWA, FUN = function(x) mean(x, na.rm = T)),
                 UTD$AWA)
############################################################################################


# Take mean of all the TOEFL values and subsitute the mean for n/a fields.
################################## For TOEFL ###############################################
ASU$TOEFL = ifelse(is.na(ASU$TOEFL),
                   ave(ASU$TOEFL, FUN = function(x) mean(x, na.rm = T)),
                   ASU$TOEFL)
clemson$TOEFL = ifelse(is.na(clemson$TOEFL),
                       ave(clemson$TOEFL, FUN = function(x) mean(x, na.rm = T)),
                       clemson$TOEFL)
IITchicago$TOEFL = ifelse(is.na(IITchicago$TOEFL),
                          ave(IITchicago$TOEFL, FUN = function(x) mean(x, na.rm = T)),
                          IITchicago$TOEFL)
MTU$TOEFL = ifelse(is.na(MTU$TOEFL),
                   ave(MTU$TOEFL, FUN = function(x) mean(x, na.rm = T)),
                   MTU$TOEFL)
NE_Boston$TOEFL = ifelse(is.na(NE_Boston$TOEFL),
                         ave(NE_Boston$TOEFL, FUN = function(x) mean(x, na.rm = T)),
                         NE_Boston$TOEFL)
RIT$TOEFL = ifelse(is.na(RIT$TOEFL),
                   ave(RIT$TOEFL, FUN = function(x) mean(x, na.rm = T)),
                   RIT$TOEFL)
U_southern_cal$TOEFL = ifelse(is.na(U_southern_cal$TOEFL),
                              ave(U_southern_cal$TOEFL, FUN = function(x) mean(x, na.rm = T)),
                              U_southern_cal$TOEFL)
UNC$TOEFL = ifelse(is.na(UNC$TOEFL),
                   ave(UNC$TOEFL, FUN = function(x) mean(x, na.rm = T)),
                   UNC$TOEFL)
UTA$TOEFL = ifelse(is.na(UTA$TOEFL),
                   ave(UTA$TOEFL, FUN = function(x) mean(x, na.rm = T)),
                   UTA$TOEFL)

UTD$TOEFL = ifelse(is.na(UTD$TOEFL),
                   ave(UTD$TOEFL, FUN = function(x) mean(x, na.rm = T)),
                   UTD$TOEFL)
#################################################################################################


# Change the categorical data to numerical values.				   
#################################### For Result #################################################
ASU$Result = factor(ASU$Result,
                    levels = c('Accept', 'Reject'),
                    labels = c(1, 0))

clemson$Result = factor(clemson$Result,
                        levels = c('Accept', 'Reject'),
                        labels = c(1, 0))						 

IITchicago$Result = factor(IITchicago$Result,
                           levels = c('Accept', 'Reject'),
                           labels = c(1, 0))

MTU$Result = factor(MTU$Result,
                    levels = c('Accept', 'Reject'),
                    labels = c(1, 0))

NE_Boston$Result = factor(NE_Boston$Result,
                          levels = c('Accept', 'Reject'),
                          labels = c(1, 0))

RIT$Result = factor(RIT$Result,
                    levels = c('Accept', 'Reject'),
                    labels = c(1, 0))

U_southern_cal$Result = factor(U_southern_cal$Result,
                               levels = c('Accept', 'Reject'),
                               labels = c(1, 0))

UNC$Result = factor(UNC$Result,
                    levels = c('Accept', 'Reject'),
                    labels = c(1, 0))						 

UTA$Result = factor(UTA$Result,
                    levels = c('Accept', 'Reject'),
                    labels = c(1, 0))

UTD$Result = factor(UTD$Result,
                    levels = c('Accept', 'Reject'),
                    labels = c(1, 0))	
############################################################################################

################################### For ASU ###############################################					
#Convert percentage to numeric value					
ASU$Percentage <- as.numeric(ASU$Percentage);

#ignore the records which contains n/a percentage values 
ASU <- ASU[which(is.na(ASU$Percentage) == FALSE),] 
ASU <- ASU[which(ASU$Major == 'CS'),c(-2,-7,-8)]

# Remove the column GRE QUANT as it is not used in preparing the model.
ASU <- ASU[,c(-3)]
###########################################################################################

################################## For Clemson ############################################
#Convert percentage to numeric value					
clemson$Percentage <- as.numeric(clemson$Percentage);

#ignore the records which contains n/a percentage values
clemson <- clemson[which(is.na(clemson$Percentage) == FALSE),]
clemson <- clemson[which(clemson$Major == 'CS'),c(-2,-7,-8)]

# Remove the column GRE QUANT as it is not used in preparing the model.
clemson <- clemson[,c(-3)]
###########################################################################################

################################# For IITchicago ##########################################
#Convert percentage to numeric value					
IITchicago$Percentage <- as.numeric(IITchicago$Percentage);

#ignore the records which contains n/a percentage values
IITchicago <- IITchicago[which(is.na(IITchicago$Percentage) == FALSE),]
IITchicago <- IITchicago[which(IITchicago$Major == 'CS'),c(-2,-7,-8)]

# Remove the column GRE QUANT as it is not used in preparing the model.
IITchicago <- IITchicago[,c(-3)]
###########################################################################################

################################# For MTU #################################################
#Convert percentage to numeric value					
MTU$Percentage <- as.numeric(MTU$Percentage);

#ignore the records which contains n/a percentage values
MTU <- MTU[which(is.na(MTU$Percentage) == FALSE),]
MTU <- MTU[which(MTU$Major == 'CS'),c(-2,-7,-8)]

# Remove the column GRE QUANT as it is not used in preparing the model.
MTU <- MTU[,c(-3)]
#############################################################################################

################################# For NE_Boston #############################################
#Convert percentage to numeric value					
NE_Boston$Percentage <- as.numeric(NE_Boston$Percentage);

#ignore the records which contains n/a percentage values
NE_Boston <- NE_Boston[which(is.na(NE_Boston$Percentage) == FALSE),]
NE_Boston <- NE_Boston[which(NE_Boston$Major == 'CS'),c(-2,-7,-8)]

# Remove the column GRE QUANT as it is not used in preparing the model.
NE_Boston <- NE_Boston[,c(-3)]
##############################################################################################

################################# For RIT ####################################################
#Convert percentage to numeric value					
RIT$Percentage <- as.numeric(RIT$Percentage);

#ignore the records which contains n/a percentage values
RIT <- RIT[which(is.na(RIT$Percentage) == FALSE),]
RIT <- RIT[which(RIT$Major == 'CS'),c(-2,-7,-8)]

# Remove the column GRE QUANT as it is not used in preparing the model.
RIT <- RIT[,c(-3)]
##############################################################################################

################################ For U_southern_cal ##########################################
#Convert percentage to numeric value					
U_southern_cal$Percentage <- as.numeric(U_southern_cal$Percentage);

#ignore the records which contains n/a percentage values
U_southern_cal <- U_southern_cal[which(is.na(U_southern_cal$Percentage) == FALSE),]
U_southern_cal <- U_southern_cal[which(U_southern_cal$Major == 'CS'),c(-2,-7,-8)]

# Remove the column GRE QUANT as it is not used in preparing the model.
U_southern_cal <- U_southern_cal[,c(-3)]
##############################################################################################

################################ For UNC ####################################################
#Convert percentage to numeric value					
UNC$Percentage <- as.numeric(UNC$Percentage);

#ignore the records which contains n/a percentage values
UNC <- UNC[which(is.na(UNC$Percentage) == FALSE),]
UNC <- UNC[which(UNC$Major == 'CS'),c(-2,-7,-8)]

# Remove the column GRE QUANT as it is not used in preparing the model.
UNC <- UNC[,c(-3)]
##############################################################################################

############################### For UTA ######################################################
#Convert percentage to numeric value					
UTA$Percentage <- as.numeric(UTA$Percentage);

#ignore the records which contains n/a percentage values
UTA <- UTA[which(is.na(UTA$Percentage) == FALSE),]
UTA <- UTA[which(UTA$Major == 'CS'),c(-2,-7,-8)]

# Remove the column GRE QUANT as it is not used in preparing the model.
UTA <- UTA[,c(-3)]
##############################################################################################

############################### For UTD ######################################################
#Convert percentage to numeric value					
UTD$Percentage <- as.numeric(UTD$Percentage);

#ignore the records which contains n/a percentage values
UTD <- UTD[which(is.na(UTD$Percentage) == FALSE),]
UTD <- UTD[which(UTD$Major == 'CS'),c(-2,-7,-8)]

# Remove the column GRE QUANT as it is not used in preparing the model.
UTD <- UTD[,c(-3)]
###############################################################################################

testdata$Percentage <- as.numeric(testdata$Percentage);
testdata <- testdata[which(is.na(testdata$Percentage) == FALSE),]

############################ Feature Scaling ##################################################
ASU[-1] = scale(ASU[-1])
clemson[-1] = scale(clemson[-1])
IITchicago[-1] = scale(IITchicago[-1])
MTU[-1] = scale(MTU[-1])
NE_Boston[-1] = scale(NE_Boston[-1])
RIT[-1] = scale(RIT[-1])
U_southern_cal[-1] = scale(U_southern_cal[-1])
UNC[-1] = scale(UNC[-1])
UTA[-1] = scale(UTA[-1])
UTD[-1] = scale(UTD[-1])
###############################################################################################

testdata = scale(testdata)

################################ Preparing the model ##########################################
install.packages('e1071')

# load the library
library(e1071) 

############################### Create model for ASU #########################################
# create a naive bayes classifier or model 
ASUclassifier <- naiveBayes(Result ~ ., data  = ASU)

# predict the test data result based on model created.
ASU_pred <- predict(ASUclassifier, newdata = testdata, type="raw")
ASU_pred <- ASU_pred[1]
ASU_pred[2] <- 'ASU' 
###############################################################################################

############################### Create model for clemson #######################################
# create a naive bayes classifier or model 
clemsonclassifier <- naiveBayes(Result ~ ., data  = clemson)

# predict the test data result based on model created.
clemson_pred <- predict(clemsonclassifier, newdata = testdata, type="raw")
clemson_pred <- clemson_pred[1]
clemson_pred[2] <- 'clemson' 
###############################################################################################

############################### Create model for IIT-chicago #########################################
# create a naive bayes classifier or model 
IITchicagoclassifier <- naiveBayes(Result ~ ., data  = IITchicago)

# predict the test data result based on model created.
IITchicago_pred <- predict(IITchicagoclassifier, newdata = testdata, type="raw")
IITchicago_pred <- IITchicago_pred[1]
IITchicago_pred[2] <- 'IITchicago' 
###############################################################################################

############################### Create model for MTU #########################################
# create a naive bayes classifier or model 
MTUclassifier <- naiveBayes(Result ~ ., data  = MTU)

# predict the test data result based on model created.
MTU_pred <- predict(MTUclassifier, newdata = testdata, type="raw")
MTU_pred <- MTU_pred[1]
MTU_pred[2] <- 'MTU' 
###############################################################################################

############################### Create model for NE_Boston #########################################
# create a naive bayes classifier or model 
NE_Bostonclassifier <- naiveBayes(Result ~ ., data  = NE_Boston)

# predict the test data result based on model created.
NE_Boston_pred <- predict(NE_Bostonclassifier, newdata = testdata, type="raw")
NE_Boston_pred <- NE_Boston_pred[1]
NE_Boston_pred[2] <- 'NE_Boston'
###############################################################################################

############################### Create model for RIT #########################################
# create a naive bayes classifier or model 
RITclassifier <- naiveBayes(Result ~ ., data  = RIT)

# predict the test data result based on model created.
RIT_pred <- predict(RITclassifier, newdata = testdata, type="raw")
RIT_pred <- RIT_pred[1]
RIT_pred[2] <- 'RIT' 
###############################################################################################

############################### Create model for U_southern_cal #########################################
# create a naive bayes classifier or model 
U_southern_calclassifier <- naiveBayes(Result ~ ., data  = U_southern_cal)

# predict the test data result based on model created.
U_southern_cal_pred <- predict(U_southern_calclassifier, newdata = testdata, type="raw")
U_southern_cal_pred <- U_southern_cal_pred[1]
U_southern_cal_pred[2] <- 'U_southern_cal' 
###############################################################################################

############################### Create model for UNC #########################################
# create a naive bayes classifier or model 
UNCclassifier <- naiveBayes(Result ~ ., data  = UNC)

# predict the test data result based on model created.
UNC_pred <- predict(UNCclassifier, newdata = testdata, type="raw")
UNC_pred <- UNC_pred[1]
UNC_pred[2] <- 'UNC' 
###############################################################################################

############################### Create model for UTA #########################################
# create a naive bayes classifier or model 
UTAclassifier <- naiveBayes(Result ~ ., data  = UTA)

# predict the test data result based on model created.
UTA_pred <- predict(UTAclassifier, newdata = testdata, type="raw")
UTA_pred <- UTA_pred[1]
UTA_pred[2] <- 'UTA' 
###############################################################################################

############################### Create model for UTD #########################################
# create a naive bayes classifier or model 
UTDclassifier <- naiveBayes(Result ~ ., data  = UTD)

# predict the test data result based on model created.
UTD_pred <- predict(UTDclassifier, newdata = testdata, type="raw")
UTD_pred <- UTD_pred[1]
UTD_pred[2] <- 'UTD'
###############################################################################################

# Combining all the predictions into one data frame
mydata <- data.frame(rbind(UTA_pred,UTD_pred,
                           UNC_pred,U_southern_cal_pred,RIT_pred,
                           NE_Boston_pred,MTU_pred,IITchicago_pred,
                           clemson_pred,ASU_pred))

mydata$X1 <- as.numeric(as.matrix(mydata$X1))

# Plot all the probabilities for the student 
plot(mydata$X1, main="Student Selection ", xlab="University ", ylab="Probability ", pch=19)
text(mydata$X1,labels=mydata$X2)

install.packages("eeptools")
library(eeptools)

# Sort all the probability in descending order
sorted_data<-mydata[order(-mydata$X1), ]
sorted_data

# Plot the graph with the sorted probabilities
plot(sorted_data$X1, main="Student Selection ", xlab="University ", ylab="Probability ", pch=19)
text(sorted_data$X1,labels=sorted_data$X2)