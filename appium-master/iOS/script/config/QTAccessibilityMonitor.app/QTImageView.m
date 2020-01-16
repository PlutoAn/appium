//
//  QTImageView.m
//  QTRadio
//
//  Created by fminor on 9/1/15.
//  Copyright (c) 2015 Markphone Culture Media Co.Ltd. All rights reserved.
//

#import "QTImageView.h"

#define DEFAULT_ANIMATION_DURATION              0.5f
#define DEFAULT_ANIMATION_TYPE                  UIViewAnimationOptionTransitionCrossDissolve
#define DEFAULT_TRANSITION_TYPE                 QTImageTransitiontypeFromPlaceHolder

@implementation QTImageView

#pragma mark - UIView method

- (instancetype)init
{
    self = [super init];
    if ( self ) {
        _frontImageView = [[UIImageView alloc] init];
        _backImageView = [[UIImageView alloc] init];
        
        [_frontImageView setUserInteractionEnabled:NO];
        [_backImageView setUserInteractionEnabled:NO];
        
        _imageContainer = [[UIView alloc] init];
        [_imageContainer addSubview:_frontImageView];
        [self addSubview:_imageContainer];
        
        [self _initProperties];
    }
    return self;
}

- (instancetype)initWithFrame:(CGRect)frame
{
    self = [super initWithFrame:frame];
    if ( self ) {
        CGRect _bounds = CGRectMake(0, 0, frame.size.width, frame.size.height);
        _frontImageView = [[UIImageView alloc] initWithFrame:_bounds];
        _backImageView = [[UIImageView alloc] initWithFrame:_bounds];
        _imageContainer = [[UIView alloc] initWithFrame:_bounds];
        
        [_frontImageView setUserInteractionEnabled:NO];
        [_backImageView setUserInteractionEnabled:NO];
        
        [_imageContainer addSubview:_frontImageView];
        [self addSubview:_imageContainer];
        
        [self _initProperties];
    }
    return self;
}

- (void)_initProperties
{
    _animationDuration = DEFAULT_ANIMATION_DURATION;
    _animationType = DEFAULT_ANIMATION_TYPE;
    _transitionType = DEFAULT_TRANSITION_TYPE;
    [self setUserInteractionEnabled:NO];
}

- (void)setFrame:(CGRect)frame
{
    [super setFrame:frame];
    [_frontImageView setFrame:CGRectMake(0, 0, frame.size.width, frame.size.height)];
    [_backImageView setFrame:CGRectMake(0, 0, frame.size.width, frame.size.height)];
    [_imageContainer setFrame:CGRectMake(0, 0, frame.size.width, frame.size.height)];
}

- (void)setContentMode:(UIViewContentMode)contentMode
{
    [super setContentMode:contentMode];
    
    [_frontImageView setContentMode:contentMode];
    [_backImageView setContentMode:contentMode];
}

#pragma mark - UIImageView method

@synthesize animationType = _animationType;
@synthesize transitionType = _transitionType;
@synthesize animationDuration = _animationDuration;

@synthesize image;
- (void)setImage:(UIImage *)anImage
{
    [self _ensureFrontAndBackImage];
    [_frontImageView setImage:anImage];
}

- (void)setImageUrl:(NSURL *)url
      animationType:(UIViewAnimationOptions)animationType
{
    [self setImageUrl:url
          placeHolder:_frontImageView.image
        animationType:animationType];
}

- (void)setImageUrl:(NSURL *)url placeHolder:(UIImage *)placeHolder
{
    [self setImageUrl:url
          placeHolder:placeHolder
        animationType:UIViewAnimationOptionTransitionCrossDissolve];
}

- (void)setImageUrl:(NSURL *)url
      animationType:(UIViewAnimationOptions)animationType
     transitionType:(QTImageTransitiontype)transitionType
{
    [self setImageUrl:url
          placeHolder:_frontImageView.image
        animationType:animationType
       transitionType:_transitionType];
}

- (void)setImageUrl:(NSURL *)url
        placeHolder:(UIImage *)placeHolder
      animationType:(UIViewAnimationOptions)animationType
{
    [self setImageUrl:url
          placeHolder:placeHolder
        animationType:animationType
       transitionType:_transitionType];
}

- (void)setImageUrl:(NSURL *)url
        placeHolder:(UIImage *)placeHolder
      animationType:(UIViewAnimationOptions)animationType
     transitionType:(QTImageTransitiontype)transitionType
{
    [self _ensureFrontAndBackImage];
    switch ( transitionType ) {
        case QTImageTransitiontypeFromCurrentImage:
            if ( _frontImageView.image == nil ) {
                _frontImageView.image = placeHolder;
            }
            break;
            
        case QTImageTransitiontypeFromPlaceHolder: {
            _frontImageView.image = placeHolder;
            break;
        }
            
        default:
            break;
    }
    
    _currentLoadingUrl = url;
    [_backImageView sd_setImageWithURL:url placeholderImage:placeHolder completed:^(UIImage *anImage, NSError *error, SDImageCacheType cacheType, NSURL *imageURL) {
        
        if ( ![[imageURL absoluteString] isEqualToString:[_currentLoadingUrl absoluteString]] ) {
            return;
        }
        
        if ( cacheType == SDImageCacheTypeMemory ) {
            [self _ensureFrontAndBackImage];
            [_frontImageView setImage:anImage];
            return;
        }
        
        [UIView transitionFromView:_frontImageView toView:_backImageView
                          duration:_animationDuration
                           options:animationType | UIViewAnimationOptionAllowUserInteraction
                        completion:nil];
    }];
}

#pragma mark - inner methods

- (void)_ensureFrontAndBackImage
{
    if ( _frontImageView.superview == nil ) {
        UIImageView *_temp = _frontImageView;
        _frontImageView = _backImageView;
        _backImageView = _temp;
    }
}

@end
