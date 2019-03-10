
%./svmlin -f matlab_training_data.txt.weights example/matlab_test_data.txt example/matlab_test_labels.txt

load('/home/anjana/storage/anjana/10701/Project/cifar-10-batches-mat/test_batch.mat');
% id1=labels==0;
% %id2=~id1;
% id2=labels==1;
% % test_data_all=data(id1,:);
% % test_data_all=[test_data_all;data(id2,:)];
% % test_data_labels=ones([sum(id1)+sum(id2),1]);
% % test_data_labels(sum(id1)+1:end,:)=-1;
test_data_all=data;
filename='data/all_test_data.txt';
test_data_labels=labels+1;
fid = fopen(filename, 'wt');
for image_number=1:size(test_data_all,1)
    I=test_data_all(image_number,:);
    I=rgb2gray(reshape(I,[32,32,3]));
    regions = detectMSERFeatures(I);
    [features, valid_points] = extractFeatures(I,regions,'Upright',true);
    features=features';
    S=sparse(double(features(:)));
    [i,~,val]=find(S);
    for id=1:length(i)
        fprintf(fid, '%d:%d ', i(id),val(id));
    end
     fprintf(fid,'\n');
end
fclose(fid);



test_data_labels=zeros([10000,1]);
filename='data/all_test_labels.txt';
fid = fopen(filename, 'wt');
for i=1:length(test_data_labels)
    fprintf(fid,'%d\n',test_data_labels(i));
 
end

fclose(fid);