% Taking input for the dimension of matrix
n=input('Enter dimension of matrix : ');

% Taking input for the power
k=input('Enter power : ');

% Taking input for the matrix elements
for i=1:n
    for j=1:n
        fprintf('Enter A[%d][%d]',i,j);
        A(i,j)=input(' element');
    end
end
A=reshape(A,n,n);

% Printing the matrix
disp('Matrix A : ');
disp(A);

% Finding eigenvalues and eigenvectors
[S,D] = eig(A); % S is eigen vector matrix and D is a diagonal matrix with eigenvalues as the diagonal elements

% Computing the result A^k
A_k = S*D.^k/S;

% Printing the result
disp('Matrix A^k : ');
disp(A_k);