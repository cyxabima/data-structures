#include <iostream>
using namespace std;

class Queue
{
private:
    int *arr;
    int front, rear, capacity;

public:
    Queue(int size)
    {
        capacity = size;
        arr = new int[capacity];
        front = -1; // in python we use the value 0 because we are using other data members too such as is_full and is_empty so we do not need to use -1 as value we are not using method to check isEmpty and isFull 
        rear = -1;
    }

    ~Queue()
    {
        delete[] arr;
    }

    bool isEmpty()
    {
        return front == -1;
    }

    bool isFull()
    {
        return (front == (rear + 1) % capacity);
    }

    void enqueue(int value)
    {
        if (isFull())
        {
            cout << "Queue overflow! Cannot enqueue " << value << endl;
            return;
        }

        // first element
        if (isEmpty())
        {
            front = rear = 0;
        }
        else
        {
            rear = (rear + 1) % capacity; // this is for circular increment
        }

        arr[rear] = value;
        cout << "Enqueued: " << value << endl;
    }

    void dequeue()
    {
        if (isEmpty())
        {
            cout << "Queue underflow! Nothing to dequeue." << endl;
            return;
        }

        cout << "Dequeued: " << arr[front] << endl;

        // only one element left
        if (front == rear)
        {
            front = rear = -1;
        }
        else
        {
            front = (front + 1) % capacity;
        }
    }

    int peek()
    {
        if (isEmpty())
        {
            cout << "Queue is empty!" << endl;
            return -1;
        }
        return arr[front];
    }
};

int main()
{
    Queue q(5);

    q.enqueue(10);
    q.enqueue(20);
    q.enqueue(30);
    q.enqueue(40);

    cout << "Front element: " << q.peek() << endl;

    q.dequeue();
    q.dequeue();

    q.enqueue(50);
    q.enqueue(60);
    q.enqueue(70); // will fail (full)

    cout << "Front element: " << q.peek() << endl;

    return 0;
}